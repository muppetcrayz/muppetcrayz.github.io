from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
from pathlib import Path
F='/System/Library/Fonts/Supplemental/'
for name,file in [('Arial','Arial.ttf'),('ArialBold','Arial Bold.ttf'),('Georgia','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,F+file))
OUT=Path('output/pdf/Sage-Turner-Resume.pdf')
c=canvas.Canvas(str(OUT),pagesize=(612,792))
c.setTitle('Sage Turner | Technology Leadership')
c.setAuthor('Sage Turner')
ink=HexColor('#263d32'); muted=HexColor('#5e6a60'); line=HexColor('#cdd3c7'); paper=HexColor('#f6f5ef')
c.setFillColor(paper);c.rect(0,0,612,792,fill=1,stroke=0)
L=42; R=570; y=752
styles={
 'body':ParagraphStyle('body',fontName='Arial',fontSize=9.4,leading=12.7,textColor=ink),
 'small':ParagraphStyle('small',fontName='Arial',fontSize=8.6,leading=11.7,textColor=muted),
}
def text(s,x,y,font='Arial',size=9.4,color=ink):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,s)
def para(s,x,width,style='body',gap=0):
 global y
 p=Paragraph(s,styles[style]);w,h=p.wrap(width,700);p.drawOn(c,x,y-h);y-=h+gap

def section(n,name):
 global y
 y-=10;c.setStrokeColor(line);c.setLineWidth(.6);c.line(L,y,R,y);y-=18
 text(n,L,y,size=8,color=muted);text(name,L+23,y,'ArialBold',9)
 y-=16

def company(name):
 global y
 text(name,L,y,'ArialBold',10.7);y-=15

def role(title,date):
 global y
 text(title,L,y,'ArialBold',9.1)
 c.setFont('Arial',8.5);c.setFillColor(muted);c.drawRightString(R,y,date)
 y-=12

def bullet(s):
 global y
 text('•',L+1,y-9,size=8)
 para(escape(s),L+12,R-L-12,gap=2)

text('TECHNOLOGY LEADERSHIP',L,y,'ArialBold',8.5,muted)
y-=37
text('Sage Turner',L,y,'Georgia',33)
y-=23
text('Cincinnati, OH  |  sage.turner.1997@gmail.com  |  614.869.7617',L,y,size=9,color=muted)
c.linkURL('mailto:sage.turner.1997@gmail.com',(112,y-2,276,y+11),relative=0)
y-=16
links=[('sageturner.me','https://sageturner.me',L),('linkedin.com/in/sageturner1997','https://www.linkedin.com/in/sageturner1997/',135),('github.com/muppetcrayz','https://github.com/muppetcrayz',354)]
for label,url,x in links:
 text(label,x,y,size=8.7,color=muted);c.linkURL(url,(x,y-2,x+pdfmetrics.stringWidth(label,'Arial',8.7),y+10),relative=0)
y-=18
para('CTO and hands-on developer leading two teams totaling six people. Partners closely with clients and the CEO/owner on technology, project delivery, and marketing, with experience modernizing web and mobile applications.',L,R-L)
section('01','EXPERIENCE')
company('Lampros Labs')
role('Chief Technology Officer','May 2025 - present')
role('Software Development Manager','Oct 2023 - May 2025')
role('Lead Backend Developer','Dec 2021 - Oct 2023')
bullet('Oversee two teams totaling six people; work closely with clients and the CEO/owner on project management and delivery, and contribute to marketing efforts.')
bullet('Modernized applications across multiple client projects using LLM AI tools, improving results while substantially reducing development costs.')
bullet('Led development projects through completion and built web and mobile software using PHP, JavaScript, Dart, Python, and a range of frameworks.')
y-=6
company('Fields Research')
role('PHP Developer','May 2021 - Nov 2021')
bullet('Developed healthcare research software for government programs, internal applications, and client websites using PHP, JavaScript, and Joomla.')
y-=6
company('DubTel')
role('Project Manager','Feb 2021 - May 2021')
role('Software Development Manager','Jun 2019 - Feb 2021')
role('Lead Software Engineer','Feb 2019 - Apr 2019')
role('Junior PHP Developer','Apr 2018 - Jan 2019')
bullet('Led a small team building internal web and native mobile applications with PHP, JavaScript, Swift, and Kotlin; helped create a REST API.')
y-=6
company('Capital University')
role('Student Team Lead Desktop Support Technician','Aug 2015 - Apr 2018')
para('Promoted from Student Desktop Support Technician. Troubleshot desktop and mobile technology issues; imaged and repaired computers.',L,R-L,'small',gap=12)
company('J.P. Morgan Chase & Co.')
role('Summer Technology Intern','Jun 2017 - Aug 2017')
para('Developed internal websites with Java, JavaScript, HTML, and CSS; used Jenkins and TortoiseSVN.',L,R-L,'small')
section('02','EDUCATION')
role('University of Cincinnati','Aug 2020 - present')
para('MA in History - in progress',L,R-L,'small',gap=11)
role('Capital University','Aug 2015 - May 2018')
para('BA in History and Computer Science; minor in Math',L,R-L,'small')
section('03','TECHNICAL SKILLS')
para('PHP, JavaScript, Python, Java, Dart, Swift, Kotlin, MySQL<br/>Laravel, WordPress, WooCommerce, Flutter, React, Svelte, Bootstrap',L,R-L,'small')
print('Bottom position:',y)
assert y>30, 'Content exceeds bottom margin'
c.showPage();c.save()
print(OUT.resolve())
