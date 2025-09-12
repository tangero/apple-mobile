---
layout: default
title: Up in the clouds with iOS 5
parent: Apple Company
nav_order: 74
has_children: False
has_toc: False
people:
  - Steve Jobs
---

# Up in the clouds with iOS 5

Even before Steve Jobs took the audience through his latest presentation
of the iCloud, he focused on the upcoming fifth version of the iOS
operating system. The one that is supposed to support iCloud and benefit
from it.

However, iOS 5 was supposed to have other advantages as well. Apple
traditionally compiles a list of about two hundred improvements that the
new version of the operating system will bring to users, and this case
was no different. Among these features was extended support for
emoticons, which are not always functions of fundamental importance.
However, the number 200 looks good---enough to make users switch to the
new version, but not enough to make them afraid of it.

The most important change is supposed to be the Notification Center. At
that time, the notification system was already inadequate. Notifications
via Apple servers had become so widespread and popular that the approach
Apple had initially introduced for them, namely that newer notifications
replaced older ones, which could not be accessed, was completely
unsatisfactory. And since Android and webOS had already solved the
notification issue, and it was clear that without them, the further
development of online applications on iOS would not move forward, Apple
had to work hard on them. It did so in such an interesting way that we
will discuss notifications in more detail later.

Another important new feature is iMessage. iMessage allows you to send a
text message to another iOS device via a data network instead of SMS,
and it does so transparently, so the user doesn't have to worry about
anything. If the recipient of the message has an iOS device that
supports iMessage, the message is sent via a data channel, not as an SMS
message. And it doesn't have to be just text; you can also send photos,
videos, contacts, or even your location. A blue dot indicates that you
can send an iMessage to the recipient instead of an SMS message.

What does this mean? Further liberation from the power of the
telecommunications industry, from the reach of paid SMS messages. And a
little surprise: it was assumed that Apple would try to push its iChat,
but it apparently realized that the service was not widely used and that
it would be better to give up on promoting it for mobile phones. So far,
iMessage has been very well received by users and its use is
significantly more widespread than FaceTime calls. Apple has capitalized
on the popularity of existing applications such as Kik and WhatsApp,
which offered a very similar service two years earlier, albeit not as
elegantly integrated into the system, and on multiple platforms. The
expansion of iMessage would benefit if Apple documented and published
its protocol. As with FaceTime (or Google Talk, for example), it is an
implementation of XMPP, which is also used for notification
transmission, so strong cross-linking of iMessage, FaceTime, and system
and application notifications is very likely in the future, especially
if Apple senses user demand.

At the end of February 2012, Apple released iMessage as a standalone
client program for Mac (in beta), and iMessage is set to be part of the
new Mountain Lion 10.8 operating system, which is due to hit the market
in summer 2012. The desktop version allows communication with all
iMessage installations, including those on iPhone, iPad, or iPod
Touch---and, of course, between desktop computers. Another nice feature
is that it can also be used for communication within Google Talk, AIM,
and Yahoo.

For Apple, this is also an open door to the world of computer telephony,
where Google has its Talk and Voice services, Microsoft has bought Skype
-- and Apple needs to have its own convincing strategy. Spreading
notification services across a unified XMPP system at the core of the
system not only saves device resources, but also leaves enough room for
further development, as can be seen from the upcoming integration into
the OS X operating system.

A nice little feature of the new system is the separation of digital
newspaper and magazine subscriptions into a separate Newsstand
application. Apple is emphasizing that the sale of digital content is a
high priority, but it has not yet been as successful in digital books,
newspapers, and magazines as its competitor Amazon and its Kindle
platform.

Twitter integration is also a new feature that not everyone will use.
Synchronization with Mac or PC via WiFi is now available, so there is no
need to connect the device with a USB cable. Apple is improving photo
editing, adding editing options, and improving camera and calendar
functionality. There are a number of small and useful features that are
not worth going into in detail. But to conclude our discussion of iOS,
let's take a look at the biggest change: notifications.

**The story of the missing dashboard and the multitasking and
notification system**

Do you know why iPhones and iPads don't have a dashboard, i.e., that
home screen that summarizes who just called you, where your emails came
from, and how many entries you have in your calendar?

It's an interesting story that illustrates the principles of iOS
design. In reviews, authors usually mention the absence of a dashboard
as a major drawback of the iOS platform. It doesn't have a dashboard,
so it's not suitable for professional use, it's just for fiddling
around with your finger. Reviewers usually used Palm or WinCE before,
where a dashboard is or can be, and now they miss it.

From the outset, the iPhone was aimed at users who had not yet owned a
smartphone because they found them too complicated and useless for
everyday tasks. One of the breakthroughs in UI research for the iPhone
(at that time, only the iPhone) was the realization that dashboards are
generally not useful for ordinary people. Why? Because it represents a
jumble of events thrown together without any meaningful sorting. And it
also causes stress. Whenever the user looks at the display, they see a
pile of unfinished tasks, unread emails, and calendar entries.
Frustration.

An internal Apple survey showed that the average user thinks,
[]{dir="rtl"}"I want to see what I need to do today, so I'll go to my
calendar. And ["]{dir="rtl"}when I want to see my emails, I'll go to
my emails." Along with notifications that let you know you're about to
leave for a meeting, Apple has left the sorting of events up to the
user. And on the fact that they know they use Evernote for notes and are
willing to go into it and don't need to see the latest notes on the
home screen. Users usually never need to see the latest notes, they need
to see this particular note, but the system doesn't yet have a way to
recognize which one is the right "this" note.

It is a mental shift from voluntary self-bullying to management
accompanied by the prevention of mistakes through reminders and
notifications. It caught on with people.

Windows Phone 7 consciously takes a different path, and when you look at
it in detail, you realize how much smarter the iOS approach is. WP7 can
only serve you a small piece of information, just a tiny snippet, in a
tile. Just a few words from your Facebook status; it can't fit the
whole thing in there. And in those few words, you can't even tell if
you'd be interested in the rest. It's a confusing mess.

*Image: WP7 interface
Caption:

The image shows what such confusion can look like -- on the right is the
original WP7 interface, on the left the user decided to add a little
more to the system's home screen. It certainly helped him...*

The same goes for other information interfaces for mobile phones, such
as Motorola's Motoblur. Fast-moving snippets of information that were
difficult to configure and even more difficult to come up with a
meaningful configuration. For example, with Facebook statuses, it is
difficult to force Motoblur to display meaningful information. While
Facebook itself tries to figure out which statuses would interest you
and sort them (with an average of 600 friends, there's no other way),
Motoblur shoves them at you one after another because that's all it can
get from Facebook's API and it's not willing to do anything about it.
The result? The user is overwhelmed by noise and eventually gives up on
using Motoblur.

In the fifth version of iOS, Apple made a significant concession to its
previous doctrine of "no dashboard on iOS devices." And with good
reason. iOS devices are gradually finding their way into the hands of
those for whom they were not intended: data professionals,
self-destructive time managers, and technicians who want to set
everything up in detail according to their own preferences. To a certain
extent, this will work, because people and their needs are different,
but money is only one thing.

But why doesn't Apple allow users to install a dashboard as an
alternative? Why does it impose a single path?

First, it should be noted that several dashboards or alternative
launchers exist, but only for jailbroken iPhones, as they are installed
via Cydia. So this is not a limitation in the system design, but a
limitation in the system policy. Anyone who has ever installed an
unofficial dashboard will probably understand why Apple does not
officially allow them.

The reason is battery life. iOS is very obsessive when it comes to
battery life. The original ban on multitasking was not because the
operating system or processor couldn't handle more tasks, but because
there were no mechanisms to control how much battery power each
application consumed.

The solution that "enabled" multitasking was actually quite simple.
The phone system has its own internal API, to which each program passes
tasks to be performed in the background. And there is a predefined set
of these tasks: for example, reading the location and calling a program
depending on it (we know that reading the location on iOS does not
necessarily mean turning on GPS, it depends on the required accuracy).
Or, for example, listening to the Internet on a port and calling an
application if something comes in.

It is perhaps obvious why this approach is better: things that require
significant battery resources are centralized and controlled by the
operating system. There is one central unit that takes care of whether
and which ports and addresses from the network are listened to or
pinged, at intervals that the system considers optimal. If each
application took care of this separately, with five applications
running, the phone would be constantly using data and the battery would
be completely empty in a few hours, even without the user visibly using
the applications. For example, WP7 has also adopted this system to a
certain extent, while Symbian and Android do not have it, which has a
significant impact on battery life.

A normal iOS app will launch, and when you want to multitask, it will
send requests to the API to call it again (for example, an IM program
will call again when a message arrives on the port) and then clear
itself from memory. And because it hangs in the API, iOS cleverly shows
it as a live application, even though the entire IM program has been
cleared and is not running, except that it is registered in the
system's protected processes. An elegant thing that the developer
doesn't even notice. When an event occurs, such as a message arriving
in Skype, the API checks which program the message is for, calls it with
the appropriate parameters, and the Skype application is restored with
the incoming message window. The user thinks their application is
running in multitasking mode, but this is not the case. True
multitasking in iOS is reserved for certain applications only.

And what does multitasking have to do with the dashboard? For the
dashboard to work, it would have to run in the background and update
events on the home screen based on what just happened. This would give
the system control over resources to an unknown application that anyone
could cobble together as they saw fit. And it's not about the graphics,
it's about resources. A poorly programmed dashboard that updates too
often will be demanding on both the battery and the processor's
performance. And would a well-programmed dashboard reduce battery life
by a few percent rather than tens of percent? That's the first thing
iOS designers have learned: percentages are a lot, but only a few tenths
of a percent are acceptable. Add percentage to percentage and the
battery is empty in half a day, which is exactly what you don't want.

Whenever there is talk of some "monopolistic restriction" imposed by
iOS, the explanation is usually simple: it is either to reduce power
consumption, processor usage, or both. The priority of iOS devices is
maximum battery life and constant (=fast) user response. Could Apple
leave it up to users to decide what to install? Sure, it could, but then
it would end up like Symbian and Android (even Android is fighting
back), which users clutter up with all kinds of software and then wonder
why their battery dies before evening, even though when they bought the
phone, it lasted two days straight...

But how to get around users' demands for timely information about
ongoing events? In iOS 5, Apple solidly resolved the "dashboard not
allowed" dilemma with Notification Center. Immediately, voices were
heard saying that it had copied the notifications in the Android system,
because it also placed them in the top row. This comment was based on
the fact that notifications in iOS and Android look similar, but their
implementation is diametrically different.

In what way? Unlike Android, iOS has backend servers that mediate
notifications from the internet. In Android, only a running local
application can send a notification, or the developer has to solve it on
their own (and since version 2.2, for the sake of completeness, there is
the C2DM method). On iOS, this solution is designed so that the
application can register a request (e.g., listening for a new IM
message), clear itself from memory, and then restore itself to its
original state with the notification when it arrives, which gives the
impression that the application is multitasking, as we explained
earlier.

The chosen, more complex solution is also the reason why Apple struggled
with notifications for some time. Even in the current state, where
notifications in iOS4 are often useless because they "get lost" (there
was no history), 100 billion of them were sent. It was necessary to
scale up the servers and server solution, because with a meaningful
notification history, traffic can be expected to explode. The fact that
the notification is located in the top bar, as on Android, is logical --
Apple has been placing notification messages here as missed call icons
since the beginning, even before Android existed.

What is the technical difference between a notification and a dashboard?
In terms of consumption, it is quite significant. A notification
receives a message, while a dashboard queries. Querying means doing so
cyclically, which means greater consumption. Receiving a message means
only getting information about a change. It's a matter of battery
percentage, and that's not insignificant.

Apple is therefore preparing something very similar for people who
cannot do without a dashboard, but technically in the form of
notifications. Notifications are permanently present on the locked
screen of iOS5 devices and also allow messages from the internet to be
received in the form of push notifications, which are pushed, not
requested. This opens up interesting possibilities without the need to
have memory filled with running programs.

I'm not saying that Apple's approach in iOS will prove successful in
the long run, but so far it looks progressive. It's interesting to note
that BlackBerry uses similar notifications, and ultimately, since
Android 2.2, Google has also been using Cloud to Device Messaging.

And as mentioned earlier, notifications, like iMessage and FaceTime, are
based on the XMPP protocol, so the possibilities for cross-platform
communication and status information transfer via XMPP, which is
included directly in the system, are extensive and provide Apple with
room for future development.

In February 2012, Apple introduced a new version of its OS X 10.8
operating system for its computers, called Mountain Lion, which includes
Notification Center (and a number of other new features) integrated into
the system and across all user devices via the company's iCloud.