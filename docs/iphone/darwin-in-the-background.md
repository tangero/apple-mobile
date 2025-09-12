---
layout: default
title: Darwin in the background
parent: iPhone Revolution
nav_order: 21
has_children: False
has_toc: False
year: 1997
products:
  - NeXT
---

# Darwin in the background

Here we need to make another detour towards the Darwin operating system.
When Apple bought Jobs' NeXT company in 1997, the transaction naturally
included the NeXTSTEP operating system and its variant created in
cooperation with Sun Microsystems and called OpenSTEP. The NeXTSTEP
operating system was also supposed to become the basis for Apple's new
operating system, which was one of the reasons Apple bought Jobs' NeXT.
The attractive and perhaps underappreciated charm of NeXTSTEP at the
time was its multi-platform capability; the system could run on the
Intel x86 platform as well as on Motorola 68K, PA-RISC, and SPARC, i.e.,
virtually all processors used by desktop platforms at the time. It was
also possible to create distribution files containing binary versions of
the program for all processor platforms, known as fat binaries.

The legacy of NeXT thus served as the basis for the development of a new
operating system called Rhapsody, which Apple first unveiled at a
developer conference in 1997. This system brought a number of changes
compared to previous versions of Mac OS, the most notable of which, in
our view, were the following:

•The kernel and related subsystems were based on Mach and BSD.

•subsystem compatible with the previous Mac OS (Blue Box) -- later known
as the Classic interface

•extended implementation of the OpenStep API (Yellow Box) -- later
developed into Cocoa.

•Java virtual machine

•window system based on Display PostScript

•interface based on Mac OS, but combined with OpenSTEP

Apple planned to transfer most of the software frameworks from Mac OS,
such as QuickTime, QuickDraw 3D, QuickDraw GX, and ColorSync, as well as
file systems from the original Apple computers, Apple Filing Protocol
(AFP), HFS, UFS, and others, to Rhapsody. However, it soon became
apparent that this was no easy task. The first developer release (DR1)
in September 1997 was followed by a second DR2 in May 1998, but there
was still a lot of work to be done. The first developer preview
(Developer Preview 1) came a year later, in May 1999, and by then the
system was called Mac OS X. A month earlier, Apple had spun off the
server version, Mac OS X Server 1, which it officially released, as well
as an opensource version Darwin, thereby fulfilling (to a large extent,
which was heavily criticized and debated) the condition of releasing the
source code of the system, which uses other open source components that
require this and which Apple included in its system when it was based on
the Mach and BSD kernels.

Darwin is essentially Mac OS X without a graphical interface and without
a number of proprietary libraries, such as FairPlay music file security.
You can download it; since later versions are only available as source
files, not binary versions, you can compile them and run them as an
operating system on a wide range of processor platforms. Darwin will
serve two purposes for Apple in the future: it will be a constant
reminder that porting the Mac OS X operating system to another processor
platform will not be so difficult as to be impossible. And it will be a
response to objections that Apple software is closed and proprietary, an
impression that Apple will later give rise to, especially in Europe. In
America, where it is more widespread in education and Darwin is commonly
used on many school servers, awareness of the openness and use of
standard components in Apple software is much greater. Darwin is still
the core of every Mac OS X system and has a fairly large group of
contributors to its open source development, with this development
feeding back into the core of Mac OS X.

The first stable version of Mac OS X 10.0, nicknamed Cheetah, was
released in March 2001, four years after the start of development of
Rhapsody, which was expected to be easily converted for use on the Apple
platform. This irony caused the company a number of problems, as it
forced its users to use the unsatisfactory and unpromising Mac OS
platform for those four years.

Darwin thus became the basis for the operating system within the Purple
2 project. At a time when it was unclear whether Apple would opt for ARM
processors, which it had helped design, or Intel, which it had just
started using in desktops, this was a very wise choice, as it allowed
the processor platform to be changed without much pain, as Apple was
doing with PowerPC and Intel. In addition, it was a compact and proven
system to which an interface (API) needed to be added---in this case,
Cocoa Touch, a touch-optimized OpenSTEP API with a library for working
with mobile phones.

Ultimately, a design was created that divided the system into four
abstraction layers:

•system kernel layer

•core services layer

•media layer

•Cocoa Touch touch interface layer

Why was this important and noteworthy? Jobs believed that a mobile phone
must respond perfectly to user requests. If the user presses a button,
the phone must respond. It must clearly confirm that it has accepted the
user's input, and the best way to do this is by performing the desired
function. One of the developers demonstrated this approach to Jobs on a
Nokia phone running Symbian, where the phone responded too slowly when a
selection was pressed. The user swiped a name in the list and
accidentally called another name. This was frustrating for Jobs, and he
didn't want to see anything like that on his mobile phone. The
operating system had to prioritize processing the user's selection, and
the Cocoa Touch touch interface had the highest priority in the system.
Only after that did the other layers of the system have priority. If the
user made a selection or input, something had to happen to reassure the
user that everything was proceeding smoothly. Another argument for this
approach was the "bouncing icons" in desktop Mac OS X. When the user
launched a program from the system dock, nothing visible usually
happened for a while until the program was loaded from the disk into the
computer's operating memory. Users would click on the icon repeatedly
because they didn't know that the program was already loading into
memory. The developers solved this by making the icon bounce until the
program was fully loaded into memory. In the mobile version, it was
necessary for the system to respond immediately to any user input in a
similar way.

This approach subsequently became so ingrained in the mobile system that
even individual functions within Cocoa Touch are processed in the system
with different priority classes so that the user has the best possible
impression of the phone running smoothly.

At that time, Apple was not yet seriously considering the possibility of
running third-party applications on the phone. In fact, it was not even
desirable at that time. The upcoming operating system was, of course,
fully supportive of preemptive multitasking, memory protection, and
other advanced features of modern operating systems, which was in
contrast to other operating systems at the time that struggled with
memory protection (Symbian), multitasking (Palm OS), or both (Win CE).
However, Jobs primarily viewed the upcoming mobile phone as a device
intended for consuming music supplied by Apple. Third-party applications
would only slow things down, and Jobs realized that a number of details
would need to be worked out, such as the distribution system, so even
though mobile OS X natively supported the ability to run additional
applications in the background, Apple artificially limited this option.
When the iPhone hit the market, only "jailbroken" phones, i.e., phones
that had been stripped of this protection, could install emerging
third-party applications. Long after the iPhone's launch in January
2007, Jobs assumed that developers would create exclusively web-based
applications and that only Apple would create native applications.

However, in the summer of 2006, the development of the mobile version of
OS X was still in a completely unsatisfactory state. Although the basic
porting of the system was completed in record time by a team of only two
engineers, the integration and coordination of the individual elements
of the mobile phone interface was dire. Calls dropped, the software
often crashed, and battery life was unreasonably low. While 200 people
were working on the project in September 2005, that number quickly grew
to 500 in two parallel teams, but it was still not enough. A serious
disadvantage was the secrecy in which Apple worked: new people could not
be recruited through public recruitment, but only through
recommendations, often via intermediaries. For example, the testing part
of the software team was largely virtual, with prototyping and testing
carried out by people who communicated primarily by email and did not
even know they were working for Apple for a long time. That's how
secretive it was.

There is a story about one of the user interface development project
managers who believed he was working on interface changes in the Symbian
system licensed by Samsung -- that's how strict the secrecy was. He
worked remotely and had a contract with a law firm representing the
"customer." One day, his supervisor asked him for his cell phone
number, saying that a message with recommendations for the interface had
arrived on the desk of the top boss, who had a habit of asking the
people working on the task directly for details that interested him.
When the developer working from Europe received a late-night call from
an American number and the caller began asking why he had not
recommended one of the options due to legal issues, the developer
pointed out that this method infringed on Apple's patents and that he
doubted Jobs would sell the rights. There was a moment of silence on the
line, and then the caller asked with a laugh, "You have no idea who's
calling you, do you?"

Since spring 2006, Apple had intensified its recruitment of developers,
but still had limited capacity available, which contrasted with Steve
Jobs signing a cooperation agreement with Cingular in July 2006.
Cingular was to invest substantial funds in expanding its mobile network
and supporting data services, as well as investing a significant amount
in supporting and selling the new Apple phone. In return, it was to
receive a share of the money earned from orders placed on the iTunes
Store and five years of exclusivity on the US market for the sale of the
phone. Along with this, Cingular committed to working with Apple on the
development of a visual voicemail system. Apple was betting that users
would want to use voicemail in the same way they used email, and that,
along with email and a web browser, it would be one of the most
interesting new features added to the phone and iPod. Cingular committed
to launching the mobile phone and investing millions of dollars in its
promotion, but no one in the company's management had actually seen the
mobile phone itself. Such was the belief in Apple's success and Steve
Jobs' persuasiveness, even though Cingular had already had one bad
experience with the Rokr project, which was led by Motorola.

The contract with Cingular was supposed to remind Jobs of the
seriousness of the situation. Apple needed a new selling point,
otherwise the iPod and iTunes revenues would slowly disappear, replaced
by mobile phones equipped with MP3 players. When even another wave of
recruitment failed to improve the situation in the software development
team, Jobs took an unusual step: he transferred the developers who were
working on the new version of the Mac OS X 10.5 Leopard desktop
operating system to the team developing the mobile version. This
kick-started its development, but delayed the regular release of new
versions by six months. When Jobs explained this event a year later at a
meeting with investors, he emphasized that it was his decision, and he
was rewarded with thunderous applause. The courage with which he
prioritized the development of the mobile system paid off, but it also
meant that many users of the Mac desktop platform would be unable to
shake the impression that computers were now taking a back seat to
Apple's mobile platform.

In November 2006, at the launch of Cingular Music, Cingular CEO Robert
Hyatt responded to journalists' questions about whether he was planning
to launch the iPhone with Apple by saying that he knew nothing about it
and had never seen such a device. He wasn't lying. It wasn't until
December 11, 2006, that Steve Jobs showed a prototype of the iPhone to
Cingular representatives at the Four Seasons hotel in Las Vegas. It was
already a relatively stable prototype that Jobs had been using
personally for several weeks, which, incidentally, resulted in the need
to replace the plexiglass cover of the display with real glass. The
plastic cover scratched easily, which Jobs hated, so he pushed for the
search for "gorilla glass." However, even when the phone was unveiled
in January 2007, it was not clear whether it would be possible to
replace the glass in mass-produced phones, as drop tests had not been
completed.

By mid-December, Jobs was convinced that the company was capable of
resolving all potential problems with launching the product and that it
would be possible to unveil the phone at MacWorld in January, the most
appropriate and dignified date for presenting this sensational new
product eagerly awaited by fans. Although development was far from
complete, he decided on another trick to keep the attention of an
already tense audience and market: he would introduce the product but
not immediately put it on sale with the announcement, as had been the
custom until then. Instead, the company would allow itself a six-month
delay, citing the necessary approval process by the US regulator, the
FCC.