from pathlib import Path
p=Path('index.html'); s=p.read_text()
s=s.replace('Student ID / Code (Optional)</label>\n          <input type="text" id="studentCode" placeholder="e.g. TT-8842">','Student ID / Code * <span style="font-weight:400">(new student: 000)</span></label>\n          <input type="text" id="studentCode" required placeholder="e.g. 1693 or 000">')
s=s.replace("""    window.addEventListener('DOMContentLoaded', () => {
      const levelSelect = document.getElementById('initialLevel');
      currentLevel = levelSelect ? levelSelect.value : 'BEG';
      preloadLevelAudioBank(currentLevel);
    });""","""    window.addEventListener('DOMContentLoaded', () => {
      const q=new URLSearchParams(location.search), set=(id,...keys)=>{for(const k of keys){const v=q.get(k);if(v){document.getElementById(id).value=v;break;}}};
      set('studentCode','studentId','studentCode','id'); set('studentName','fullName','name'); set('studentPhone','phone','whatsapp');
      const levelSelect=document.getElementById('initialLevel'), urlLevel=(q.get('level')||'').toUpperCase();
      if(levelSelect&&['SM','BEG','INT','ADV'].includes(urlLevel)) levelSelect.value=urlLevel;
      currentLevel=levelSelect?levelSelect.value:'BEG'; preloadLevelAudioBank(currentLevel);
    });""")
s=s.replace("""    function startAssessment(event) {
      if (event) event.preventDefault();""","""    function startAssessment(event) {
      if(event){const form=event.currentTarget;if(form&&!form.checkValidity()){form.reportValidity();return;}event.preventDefault();}""")
s=s.replace("""    function submitTest() {
      const durationSec = Math.round((new Date() - startTime) / 1000);""","""    function submitTest() {
      const sid=document.getElementById('studentCode')?.value?.trim(), nm=document.getElementById('studentName')?.value?.trim(), ph=document.getElementById('studentPhone')?.value?.trim();
      if(!sid||!nm||!ph){alert('Student ID, full name and phone are required.');return;}
      const durationSec = Math.round((new Date() - startTime) / 1000);""")
s=s.replace('Build ID: 2026-08-10-FINAL-02','Build ID: 2026-08-28-IDENTITY-HOTFIX-01')
p.write_text(s)
print('patched', p)
