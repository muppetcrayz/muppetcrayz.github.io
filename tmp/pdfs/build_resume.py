from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
F='/System/Library/Fonts/Supplemental/'
for name,file in [('Arial','Arial.ttf'),('ArialBold','Arial Bold.ttf'),('Georgia','Georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,F+file))
c=canvas.Canvas('output/pdf/Sage-Turner-Resume.pdf',pagesize=(612,792))
c.setTitle('Sage Turner | Technology Leadership');c.setAuthor('Sage Turner')
ink=HexColor('#263d32');muted=HexColor('#5e6a60');line=HexColor('#cdd3c7');paper=HexColor('#f6f5ef');accent=HexColor('#789169')
c.setFillColor(paper);c.rect(0,0,612,792,fill=1,stroke=0)
L=38;R=574;X=133;y=754
styles={k:ParagraphStyle(k,fontName='Arial',fontSize=size,leading=leading,textColor=color) for k,size,leading,color in [('body',9.3,12.3,ink),('small',8.8,11.7,muted)]}
def text(s,x,baseline,font='Arial',size=9.3,color=ink):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,baseline,s)
def para(s,x=X,width=None,style='body',gap=0):
 global y
 p=Paragraph(s,styles[style]);_,h=p.wrap(width or R-x,700);p.drawOn(c,x,y-h);y-=h+gap

def section(n,label):
 global y
 y-=10;c.setStrokeColor(line);c.setLineWidth(.6);c.line(L,y,R,y);y-=16
 text(n,L,y-8,size=7.5,color=muted);text(label,L+17,y-8,'ArialBold',8.1)
def company(s):
 global y
 text(s,X,y-10,'ArialBold',11);y-=22

def roles(items,timeline=False):
 global y
 top=y
 for i,(title,date) in enumerate(items):
  x=X+12 if timeline else X
  font='ArialBold' if i==0 else 'Arial'
  datewidth=pdfmetrics.stringWidth(date,'Arial',8.1)
  available=R-x-datewidth-12
  if pdfmetrics.stringWidth(title,font,9)>available:
   # Preserve the complete title while giving dates their own aligned line.
   text(title,x,y-9,font,9);y-=12
   text(date,x,y-8,size=8.1,color=muted);y-=13
  else:
   text(title,x,y-9,font,9)
   c.setFillColor(muted);c.setFont('Arial',8.1);c.drawRightString(R,y-9,date);y-=15
  if timeline:
   c.setFillColor(accent);c.circle(X+2,y+9,2,fill=1,stroke=0)
 if timeline:
  c.setStrokeColor(line);c.setLineWidth(.65);c.line(X+2,top-4,X+2,y+9)
 y+=1

def bullet(s):
 global y
 text('•',X,y-9,size=8,color=accent);para(escape(s),X+11,gap=3)
def gap(n=9):
 global y
 y-=n

text('TECHNOLOGY LEADERSHIP',L,y,'ArialBold',8.3,muted);y-=35
text('Sage Turner',L,y,'Georgia',33);y-=23
text('Cincinnati, OH  |  sage.turner.1997@gmail.com  |  614.869.7617',L,y,size=9,color=muted)
y-=16
for label,url,x in [('sageturner.me','https://sageturner.me',L),('linkedin.com/in/sageturner1997','https://www.linkedin.com/in/sageturner1997/',133),('github.com/muppetcrayz','https://github.com/muppetcrayz',355)]:
 text(label,x,y,size=8.6,color=muted);c.linkURL(url,(x,y-2,x+pdfmetrics.stringWidth(label,'Arial',8.6),y+10),relative=0)
y-=15
para('Technology leader with hands-on expertise in web and mobile development. Leads two teams and works closely with clients and the CEO/owner to guide projects from planning through delivery, improve applications, and reduce development costs.',L,R-L)
section('01','Experience')
company('Lampros Labs')
roles([('Chief Technology Officer','May 2025 - present'),('Software Development Manager','Oct 2023 - May 2025'),('Lead Backend Developer','Dec 2021 - Oct 2023')],True)
bullet('Lead six people across two teams, partnering with clients and the CEO/owner on project planning, coordination, and delivery; contribute to company marketing.')
bullet('Modernized applications across multiple client projects with LLM-assisted development, improving results while substantially reducing costs.')
bullet('Delivered web and mobile projects with hands-on development in PHP, JavaScript, Dart, and Python.')
gap(7)
company('Fields Research')
roles([('PHP Developer','May 2021 - Nov 2021')])
para('Built healthcare research software for government programs, internal applications, and client websites using PHP, JavaScript, and Joomla.',gap=0)
gap()
company('DubTel')
roles([('Project Manager','Feb 2021 - May 2021'),('Software Development Manager','Jun 2019 - Feb 2021'),('Lead Software Engineer','Feb 2019 - Apr 2019'),('Junior PHP Developer','Apr 2018 - Jan 2019')],True)
para('Led a small team developing web and native mobile applications in PHP, JavaScript, Swift, and Kotlin; contributed to a REST API.')
gap()
company('Capital University')
roles([('Student Team Lead Desktop Support Technician','Aug 2015 - Apr 2018')])
para('Promoted from Student Desktop Support Technician. Resolved desktop and mobile technology issues; imaged and repaired computers.',style='small')
gap()
company('J.P. Morgan Chase & Co.')
roles([('Summer Technology Intern','Jun 2017 - Aug 2017')])
para('Built internal websites with Java, JavaScript, HTML, and CSS; used Jenkins and TortoiseSVN.',style='small')
section('02','Education')
roles([('University of Cincinnati','Aug 2020 - present')])
para('MA in History - in progress',style='small',gap=7)
roles([('Capital University','Aug 2015 - May 2018')])
para('BA in History and Computer Science; minor in Math',style='small')
section('03','Tools')
para('PHP · JavaScript · Python · Java · Dart · Swift · Kotlin · MySQL<br/>Laravel · WordPress · WooCommerce · Flutter · React · Svelte · Bootstrap',style='small')
print('Bottom:',y)
assert y>=28
c.showPage();c.save()
