'use strict';
const questions = [
  {name:'Hunger', question:'Could you be hungry?', hint:'An empty feeling, irritability, or trouble focusing can be a clue. You don’t have to be sure.', title:'Let’s get something to eat.', steps:['Pick an easy food you have available. A snack counts; it doesn’t need to be a whole meal.','Eat what feels manageable. Give yourself a few minutes before checking in again.'], tiny:'Try a bite of something easy, or ask someone to bring you a snack.'},
  {name:'Thirst', question:'Could you use a drink?', hint:'Check for a dry mouth, or think about when you last had something to drink.', title:'A few sips are a start.', steps:['Get a drink that fits your usual care plan. Put it within easy reach.','Take a few comfortable sips. There’s no need to finish it all at once.'], tiny:'Just bring your drink closer and take one sip.'},
  {name:'Bathroom', question:'Do you need the bathroom?', hint:'It’s okay to pause what you’re doing and check.', title:'Take a bathroom break.', steps:['Go to the bathroom when you can. Take your time.','Wash your hands, then get comfortable again.'], tiny:'If getting there is difficult, ask for help or clear a path first.'},
  {name:'Tired', question:'Are you tired?', hint:'Heavy eyes, feeling overwhelmed, or everything taking extra effort can be signs.', title:'You’re allowed to rest.', steps:['Find somewhere comfortable and let your body rest. Lower the lights or put your screen down if that helps.','If you can sleep, let yourself. If you can’t, a quiet break still counts.'], tiny:'Lean back, relax your shoulders, and close your eyes for a moment if that feels comfortable.'},
  {name:'Heart hurt', question:'Does your heart hurt?', hint:'For your familiar POTS chest discomfort, check in with your usual care plan.', title:'Time for electrolytes.', steps:['Get your usual electrolyte drink and prepare it as directed in your POTS care plan.','Sip it at your own pace and rest somewhere comfortable. Give yourself a little time to check how you feel.'], tiny:'Bring your electrolytes within reach, or ask someone to make your drink.', note:'This step is for your familiar symptoms. If chest pain is new, different, severe, or comes with severe trouble breathing, get urgent medical help. <a href="https://www.nhs.uk/symptoms/chest-pain/">About chest pain</a>.'},
  {name:'Head hurt', question:'Does your head hurt?', hint:'Notice any headache, pressure, or sensitivity to light or sound.', title:'Make things gentler for your head.', steps:['Turn down bright light and noise. Rest your eyes somewhere comfortable.','Try your usual headache care plan, if you have one. If pain persists or worries you, contact a clinician.'], tiny:'Lower your screen brightness and look away from it for a little while.', note:'A sudden, extremely painful headache, or a headache with new weakness or trouble speaking, needs emergency medical help. <a href="https://www.nhs.uk/symptoms/headaches/">About headaches</a>.'},
  {name:'Body pain', question:'Is your body hurting?', hint:'Check your jaw, shoulders, back, stomach, and anywhere else asking for attention.', title:'Give the sore part some support.', steps:['Shift into a position that feels better. Try a pillow or loosen anything pressing on you.','Follow your usual pain care plan. Stop any movement that makes the pain worse. Seek medical advice for new, worsening, or concerning pain.'], tiny:'Unclench your jaw and support one uncomfortable part of your body.'},
  {name:'Clothes', question:'Are your clothes uncomfortable?', hint:'Think about tight waistbands, seams, tags, socks, or fabric that feels wrong.', title:'Comfort is a good enough reason.', steps:['Loosen, adjust, or change whatever is bothering you. Soft clothes or fewer layers might help.','Check again once you’ve changed. You don’t have to put up with an irritating texture.'], tiny:'Adjust just the most annoying seam, tag, or waistband.'},
  {name:'Hair, jewelry & makeup', question:'Is anything on you bothering you?', hint:'Check your hair, jewelry, and makeup. Pulling, pressure, or stickiness can add up.', title:'Take off a little discomfort.', steps:['Loosen your hair, remove a piece of jewelry, or gently take off makeup if it’s bothering you.','Choose whatever feels easiest. You don’t need to redo your appearance afterward.'], tiny:'Remove or loosen the one thing you notice most.'},
  {name:'Temperature', question:'Are you too cold or too hot?', hint:'Notice your hands, feet, face, and the room around you.', title:'Let’s adjust the temperature.', steps:['If you’re cold, try a comfortable layer, socks, or a blanket.','If you’re hot, remove a layer, use a fan, or move somewhere cooler. Make changes gently and follow your usual POTS care plan.'], tiny:'Add or remove one layer, or move away from a heat source.'},
  {name:'Dizzy', question:'Are you dizzy or lightheaded?', hint:'You can pause here. You don’t need to stand up to do this check-in.', title:'Get settled somewhere safe.', steps:['Sit or lie down somewhere safe. Avoid driving or moving around while you’re dizzy.','Follow your usual POTS care plan, including fluids or electrolytes if that’s part of it. Ask for help if you need it.'], tiny:'Stay seated or lie down, and put what you need within reach.', note:'If this feels different from your usual symptoms, persists, or worries you, seek medical advice. New weakness, trouble speaking, chest pain different from your usual pattern, or severe trouble breathing needs emergency help.'},
  {name:'Bored', question:'Could you be bored or understimulated?', hint:'Sometimes restlessness means you need something interesting, comforting, or different.', title:'Try a small change of scene.', steps:['Pick one low-effort thing: a favorite song, a simple game, a familiar show, or a small creative activity.','Try it for a few minutes. You can switch if it isn’t helping; this isn’t a commitment.'], tiny:'Put on one song you like, or send someone a low-pressure hello.'}
];
const scene = document.querySelector('#scene');
const back = document.querySelector('#back');
const restart = document.querySelector('#restart');
const history = [];
let state = {view:'welcome', index:0};
function go(view, index = state.index) { history.push({...state}); state = {view,index}; render(); }
function button(label, action, primary = false) { const el = document.createElement('button'); el.textContent = label; el.classList.toggle('primary',primary); el.addEventListener('click', action); return el; }
function next() { go(state.index === questions.length - 1 ? 'finish' : 'question', state.index + 1); }
function render(focus = true) {
 const q = questions[state.index];
 document.querySelector('.progress-wrap').hidden = state.view === 'welcome';
 document.querySelector('#progress-label').textContent = state.view === 'finish' ? 'Check-in complete' : `${Math.min(state.index + 1,12)} of 12 · ${q?.name || ''}`;
 document.querySelector('#progress').value = state.view === 'finish' ? 12 : state.index;
 back.hidden = history.length === 0; restart.hidden = state.view === 'welcome';
 let copy = ''; const actions = document.createElement('div'); actions.className = 'actions';
 if(state.view === 'welcome') {
  copy = '<p class="eyebrow">A small place to pause</p><h1 id="title" tabindex="-1">Feeling upset?<br>Let’s check in.</h1><p class="intro">You don’t have to figure everything out at once. We’ll check a few things your body might need, one question at a time.</p><p class="intro">If something fits, try one small thing. If you’re not sure, we can check anyway. There’s no rush.</p>';
  actions.append(button('Let’s start →',()=>go('question',0),true));
 } else if(state.view === 'question') {
  copy = `<p class="eyebrow">A moment to notice</p><h1 id="title" tabindex="-1">${q.question}</h1><p class="intro">${q.hint}</p>`;
  actions.append(button('Yes, that might be it',()=>go('care'),true),button('No, I’m okay here',next),button('I’m not sure — let’s check',()=>go('care')));
 } else if(state.view === 'care') {
  copy = `<p class="eyebrow">One small thing</p><h1 id="title" tabindex="-1">${q.title}</h1><ul>${q.steps.map(s=>`<li>${s}</li>`).join('')}</ul>${q.note?`<p class="note">${q.note}</p>`:''}<p class="intro">Take the time you need. Come back when you’re ready.</p>`;
  actions.append(button('I tried it →',()=>go('check'),true),button('That feels like too much',()=>go('tiny')),button('I can’t do this right now — continue',next));
 } else if(state.view === 'tiny') {
  copy = `<p class="eyebrow">Smaller is okay</p><h1 id="title" tabindex="-1">Let’s make it easier.</h1><p>${q.tiny}</p><p class="intro">You can ask for help. You can also move on and return to this later.</p>`;
  actions.append(button('I tried a small step →',()=>go('check'),true),button('Keep going',next));
 } else if(state.view === 'check') {
  copy = '<p class="eyebrow">No right answer</p><h1 id="title" tabindex="-1">How are you feeling now?</h1><p class="intro">A little better counts. It’s also okay if this wasn’t the thing you needed.</p>';
  actions.append(button('A little better — keep checking',next,true),button('About the same — keep checking',next),button('I need more time',()=>go('care')),button('I feel worse',()=>go('worse')),button('I’m ready to stop here',()=>go('finish')));
 } else if(state.view === 'worse') {
  copy = '<p class="eyebrow">Pause here</p><h1 id="title" tabindex="-1">You don’t have to push through.</h1><p>Stop anything that’s making you feel worse and settle somewhere safe. Consider asking someone you trust to sit with you or help you decide what you need.</p><p class="intro">If physical symptoms are worsening, unfamiliar, or concerning, contact a clinician. For severe symptoms or immediate danger, get emergency help.</p>';
  actions.append(button('Stop the check-in',()=>go('finish'),true),button('I’m okay to continue checking',next));
 } else {
  copy = '<p class="eyebrow">A little care counts</p><h1 id="title" tabindex="-1">You can pause here.</h1><p>You made some space to notice what you need. You don’t have to feel completely better for that to matter.</p><p class="intro">If you’re still upset, there may be more going on than these questions can cover. Try naming what happened, writing down what you wish were different, or asking someone you trust for company or practical help.</p><p class="intro">For now, pick one gentle next thing. Resting is an option.</p>';
  actions.append(button('Check in again',()=>{history.length=0;state={view:'welcome',index:0};render();},true));
 }
 scene.innerHTML = copy; scene.append(actions);
 if(focus) document.querySelector('#title').focus();
}
back.addEventListener('click',()=>{if(history.length){state=history.pop();render();}});
restart.addEventListener('click',()=>go('welcome',0));
render(false);
