Title: First Look at OCaml
Date: 2014-07-12 14:00
Category: programming
Tags: language, ocaml

I recently listened to [an episode of Software Engineering Radio][seradio-204]
in which [Anil Madhavapeddy][anil] talks about OCaml and [Mirage][openmirage].
While OCaml isn't the primary focus of the interview, the reasons it was chosen
as the basis for Mirage intrigued me enough that I was inspired to take a look.

The full text of [Real World OCaml][rwo] is available for free online, so I
dove right in and found it to be engaging and informative. I haven't quite
finished reading it yet (Part III is mostly details that aren't relevant to the
writing of small program), but within a week I was comfortable enough to start
writing a prototype [Vumi][vumi] worker in OCaml. (More on that in a future
post.)

At this point, I saw a reference to [a series of blog posts][roscidus-ocaml]
documenting [0install][0install]'s transition from Python to OCaml. They're
well worth reading for anyone interested in the costs and benefits of writing a
nontrivial software system in OCaml. While writing this post (the next
paragraph, actually) I saw a recommendation for this very useful
[beginner's guide to OCaml beginner's guides][beginner-guide] and read through
it. Both of these were mentioned in the #ocaml IRC channel on freenode, which
is probably the best programming language channel I've seen.

While I'm not yet fluent enough in OCaml to write idiomatic code, I'm far
enough along the learning curve that I'm able to solve real problems in the
language as long as I have language and library references handy. OCaml is
notable in that I've reached this point without discovering anything I hate
about it. The only other language that remained hate-free this far into the
learning process was Python, and it's still the language I'm least grumpy
about.

I'm looking forward to learning more about OCaml by (hopefully) building some
useful software in it over the next few weeks. It's certainly the language I've
been happiest about learning nearly a decade.


[seradio-204]: http://www.se-radio.net/2014/05/episode-204-anil-madhavapeddy-on-the-mirage-cloud-operating-system-and-the-ocaml-language/
[anil]: http://anil.recoil.org/
[openmirage]: http://openmirage.org/
[rwo]: https://realworldocaml.org/
[vumi]: https://github.com/praekelt/vumi
[roscidus-ocaml]: http://roscidus.com/blog/blog/categories/ocaml/
[0install]: http://zero-install.sourceforge.net/
[beginner-guide]: http://blog.nullspace.io/beginners-guide-to-ocaml-beginners-guides.html
