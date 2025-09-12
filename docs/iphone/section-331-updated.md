---
layout: default
title: Section 3.3.1 Updated
parent: iPhone Revolution
nav_order: 62
has_children: False
has_toc: False
year: 2010
products:
  - iPhone
  - iPad
people:
  - Steve Jobs
---

# Section 3.3.1 Updated

On March 8, 2010, Steve Jobs presented the new version 4.0 of the iPhone
operating system to journalists. This is only a preview; the new version
will not be available to customers until the summer. The aim is to let
people know what new features are coming and what direction development
is taking. It is also a response to the launch of the iPad tablets,
which are selling very well and are generally expected to repeat the
success of the iPhone.

How useful will the iPad be for browsing the web without Flash, Adobe
and critics asked in advance? Flash is not supported, Apple replied, and
on March 8, Steve Jobs showed that he still does not count on Adobe.
Even the new version of iPhone OS 4 will not support Flash. And only
later did the consequences of a minor change in the conditions for
approving software for the App Store become apparent.

The change in section 3.3.1 excludes from approval applications that are
launched on the iPhone using some kind of intermediate layer rather than
directly via the Cocoa Touch API. This excluded applications created
using AIR (but also those created in .NET via MonoTouch) and others.
Apple has cut off one of the selling points of Adobe CS5, which was
scheduled to be released four days later. Apple has made it clear that
applications created with AIR and other cross-platform toolkits will not
be approved in the App Store. If Flash application developers were
counting on compiling their applications in the new CS5 and releasing
them in the App Store, they are now out of luck.

The new version of the provision reads:

*3.3.1 --- Applications may only use Documented APIs in the manner
prescribed by Apple and must not use or call any private APIs.
Applications must be originally written in Objective-C, C, C++, or
JavaScript as executed by the iPhone OS WebKit engine, and only code
written in C, C++, and Objective-C may compile and directly link against
the Documented APIs (e.g., Applications that link to Documented APIs
through an intermediary translation or compatibility layer or tool are
prohibited).*