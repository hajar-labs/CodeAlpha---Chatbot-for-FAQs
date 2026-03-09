// static/chat.js — SmartHelp Frontend Logic

const API = '';  // Same origin

// ── Load FAQs into sidebar ──────────────────────────────────────────────────
async function loadSidebar() {
  try {
    const res = await fetch(`${API}/api/faqs`);
    const data = await res.json();
    const container = document.getElementById('sidebar-faqs');

    for (const [topic, questions] of Object.entries(data.topics)) {
      const label = document.createElement('div');
      label.className = 'topic-label';
      label.textContent = topic;
      container.appendChild(label);

      questions.forEach(q => {
        const chip = document.createElement('button');
        chip.className = 'faq-chip';
        chip.textContent = q.question;
        chip.addEventListener('click', () => {
          document.getElementById('qinput').value = q.question;
          sendMessage();
        });
        container.appendChild(chip);
      });
    }
  } catch (e) {
    console.error('Sidebar load failed:', e);
  }
}

// ── Utility helpers ─────────────────────────────────────────────────────────
function scrollDown() {
  const msgs = document.getElementById('messages');
  msgs.scrollTo({ top: msgs.scrollHeight, behavior: 'smooth' });
}

function escHtml(t) {
  return t
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function colorForScore(score) {
  if (score >= 0.6) return 'var(--green)';
  if (score >= 0.3) return 'var(--yellow)';
  return 'var(--red)';
}

// ── Typing indicator ────────────────────────────────────────────────────────
function addTyping() {
  const msgs = document.getElementById('messages');
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap bot';
  wrap.id = 'typing';
  wrap.innerHTML = `
    <div class="avatar">🤖</div>
    <div class="bubble bot">
      <div class="typing"><span></span><span></span><span></span></div>
    </div>`;
  msgs.appendChild(wrap);
  scrollDown();
}

function removeTyping() {
  document.getElementById('typing')?.remove();
}

// ── Message rendering ───────────────────────────────────────────────────────
function addUserMsg(text) {
  const msgs = document.getElementById('messages');
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap user';
  wrap.innerHTML = `<div class="avatar">👤</div><div class="bubble">${escHtml(text)}</div>`;
  msgs.appendChild(wrap);
  scrollDown();
}

function addBotMsg(data) {
  const msgs = document.getElementById('messages');
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap bot';

  let bubbleHTML = '';

  if (!data.matched) {
    bubbleHTML = `
      <div class="bubble">
        I couldn't find a good match for your question. Try rephrasing, or pick a topic from the sidebar.
        Contact us at <strong>support@smarthelp.io</strong> for direct assistance.
      </div>`;
  } else {
    const m = data.matched;
    const color = colorForScore(m.score);
    const pct = m.score_pct;

    let altsHTML = '';
    if (data.alternatives && data.alternatives.length > 0) {
      const altItems = data.alternatives
        .map(a => `
          <button class="alt-chip" onclick="askQuestion('${a.question.replace(/'/g, "\\'")}')">
            ${escHtml(a.question)}<span class="alt-score">${a.score_pct}%</span>
          </button>`)
        .join('');
      altsHTML = `<div class="alternatives"><div class="alt-title">ALSO CONSIDER</div>${altItems}</div>`;
    }

    bubbleHTML = `
      <div class="bubble">
        ${escHtml(m.answer)}
        <div class="confidence">
          <label>Match</label>
          <div class="meter">
            <div class="meter-fill" style="width:${pct}%;background:${color}"></div>
          </div>
          <span class="pct" style="color:${color}">${pct}%</span>
        </div>
        <div class="matched-label">
          <span class="ml">MATCHED:</span>
          <span>${escHtml(m.question)}</span>
        </div>
        ${altsHTML}
      </div>`;
  }

  wrap.innerHTML = `<div class="avatar">🤖</div>${bubbleHTML}`;
  msgs.appendChild(wrap);

  if (data.nlp_steps) {
    addNLPPanel(msgs, data);
  }

  scrollDown();
}

function addNLPPanel(container, data) {
  const s = data.nlp_steps;
  const panel = document.createElement('details');
  panel.className = 'nlp-panel';

  const rawToks = (s.tokenized || []).map(t => `<span class="tok">${t}</span>`).join('');
  const noStopToks = (s.after_stopword_removal || []).map(t => `<span class="tok">${t}</span>`).join('');
  const stemToks = (s.after_stemming || []).map(t => `<span class="tok stemmed">${t}</span>`).join('');

  panel.innerHTML = `
    <summary>🔬 NLP Pipeline Breakdown</summary>
    <div class="nlp-pipeline">
      <div class="pipeline-step">
        <div class="step-label">① Tokenized</div>
        <div class="tokens-wrap">${rawToks || '<span style="color:var(--muted)">none</span>'}</div>
      </div>
      <div class="pipeline-step">
        <div class="step-label">② Stop-words Removed</div>
        <div class="tokens-wrap">${noStopToks || '<span style="color:var(--muted)">none</span>'}</div>
      </div>
      <div class="pipeline-step">
        <div class="step-label">③ Stemmed</div>
        <div class="tokens-wrap">${stemToks || '<span style="color:var(--muted)">none</span>'}</div>
      </div>
      <div class="pipeline-step">
        <div class="step-label">④ Vocab Size</div>
        <div style="color:var(--accent2);font-size:0.63rem">
          ${data.vocabulary_size} TF-IDF features (unigrams + bigrams)
        </div>
      </div>
    </div>`;

  container.appendChild(panel);
}

// ── Send message ────────────────────────────────────────────────────────────
async function sendMessage() {
  const input = document.getElementById('qinput');
  const query = input.value.trim();
  if (!query) return;

  input.value = '';
  input.style.height = 'auto';
  addUserMsg(query);
  addTyping();

  try {
    const res = await fetch(`${API}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });
    const data = await res.json();
    removeTyping();
    addBotMsg(data);
  } catch (err) {
    removeTyping();
    const msgs = document.getElementById('messages');
    const wrap = document.createElement('div');
    wrap.className = 'msg-wrap bot';
    wrap.innerHTML = `
      <div class="avatar">🤖</div>
      <div class="bubble">
        ⚠️ Could not reach the Python backend. Make sure the Flask server is running on port 5000.
      </div>`;
    msgs.appendChild(wrap);
    scrollDown();
  }
}

function askQuestion(q) {
  document.getElementById('qinput').value = q;
  sendMessage();
}

// ── Event listeners ─────────────────────────────────────────────────────────
document.getElementById('sendbtn').addEventListener('click', sendMessage);

document.getElementById('qinput').addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

document.getElementById('qinput').addEventListener('input', function () {
  this.style.height = 'auto';
  this.style.height = Math.min(this.scrollHeight, 110) + 'px';
});

// ── Init ────────────────────────────────────────────────────────────────────
loadSidebar();

setTimeout(() => {
  const msgs = document.getElementById('messages');
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap bot';
  wrap.innerHTML = `
    <div class="avatar">🤖</div>
    <div class="bubble">
      Try asking: <em>"How do I reset my password?"</em>, <em>"What payment methods are accepted?"</em>,
      or <em>"Is my data secure?"</em><br><br>
      Every response includes a full <strong>NLP pipeline breakdown</strong> showing tokenization,
      stop-word removal, stemming, and TF-IDF scoring. 🔬
    </div>`;
  msgs.appendChild(wrap);
}, 500);