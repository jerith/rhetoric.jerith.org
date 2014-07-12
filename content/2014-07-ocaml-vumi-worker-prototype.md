Title: Prototype Vumi Worker in OCaml
Date: 2014-07-12 14:30
Category: programming
Tags: language, ocaml, vumi
Status: draft

As mentioned in a [previous post](|filename|2014-07-first-look-at-ocaml.md), I
have started building a prototype [Vumi][vumi] worker in OCaml.

I was able to define suitable types for holding vumi messages, but specifying
fields which must be present but which may contain `null` was harder than I'd
thought. I'm reasonably sure I'll be able to clean that up (possibly by
choosing different tools) when I have some more experience, but it's the first
place OCaml's type system got in my way instead of helping me.

Once I had a basic messaging module in place, I decided it was time to hook my
prototype up to a running vumi system. This is when I discovered that the only
AMQP client library ([Netamqp][netamqp]) uses blocking I/O and has a major
dependency that failed to install on my system. Since I'm much happier working
in an asynchronous event-driven environment, I (foolishly, in all likelyhood)
started working on my own AMQP client. Of the two asynchronous I/O libraries in
OCaml, I chose to use [lwt][lwt] rather than [async][async] (which is described
in [chapter 18 of Real World OCaml][rwo-ch18]) for the somewhat petty reason
that the former is rather easier to search for.


[vumi]: https://github.com/praekelt/vumi
[netamqp]: http://projects.camlcity.org/projects/netamqp.html
[lwt]: http://ocsigen.org/lwt/
[async]: https://github.com/janestreet/async
[rwo-ch18]: https://realworldocaml.org/v1/en/html/concurrent-programming-with-async.html
