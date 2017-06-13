from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from devblog.models import Post, Comment


mkdx_content1 = """
An h1 header
============

Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.
Unicode is supported.
"""

mkdx_content2 = """
An h2 header
------------

Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the actual text starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }

As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

```
define foobar() {
    print "Welcome to flavor country!";
}
```

(which makes copying & pasting easier). You can optionally mark the
delimited block for Pandoc to syntax highlight it:

```python
s = "Python syntax highlighting"
print s

import time
# Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
```
"""

mkdx_content3 = """
### An h3 header ###

Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Notice again how text always lines up on 4-space indents (including
that last line which continues item 3 above).

Here's a link to [a website](http://foo.bar), to a [local
doc](local-doc.html), and to a [section heading in the current
doc](#an-h2-header). Here's a footnote [^1].

[^1]: Footnote text goes here.

Tables can look like this:

size  material      color
----  ------------  ------------
9     leather       brown
10    hemp canvas   natural
11    glass         transparent
"""

mkdx_content4 = """
A horizontal rule follows.

***

Here's a definition list:

apples
  : Good for making applesauce.
oranges
  : Citrus!
tomatoes
  : There's no "e" in tomatoe.

Again, text is indented 4 spaces. (Put a blank line between each
term/definition pair to spread things out more.)

Here's a "line block":

| Line one
|   Line too
| Line tree

and images can be specified like so:

![example image](example-image.jpg "An exemplary image")

Inline math equations go in like so: $\omega = d\phi / dt$. Display
math should get its own line and be put in in double-dollarsigns:

$$I = \int \rho R^{2} dV$$

And note that you can backslash-escape any punctuation characters
which you wish to be displayed literally, ex.: \`foo\`, \*bar\*, etc.
"""

class Command(BaseCommand):
    args = '<no arguments>'
    help = 'Just fills the database with dummy data'

    def _create_users(self):
        admin = User.objects.create_superuser('admin', 'admin@instador.com', 'administrador')
        admin.save()

        user1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user1.save()

        user2 = User.objects.create_user('hulk', 'hoggan@hulk.com', 'hulkpassword')
        user2.save()

        user3 = User.objects.create_user('nacho', 'nacho@elmacho.com', 'machopassword')
        user3.save()

    def _create_posts(self):
        posts=[
        Post(author_id=1, title="Dummy Post 1", content=mkdx_content2),
        Post(author_id=2, title="Dummy Post 2", content=mkdx_content1),
        Post(author_id=2, title="Dummy Post 3", content=mkdx_content3),
        Post(author_id=1, title="Another Dummy Post", content=mkdx_content2),
        Post(author_id=2, title="One more Dummy Post", content=mkdx_content1),
        Post(author_id=1, title="And another Dummy Post", content=mkdx_content4),
        Post(author_id=3, title="Just one more Dummy Post", content=mkdx_content1),
        Post(author_id=3, title="Wtf more Posts Dummy Post", content=mkdx_content2),
        Post(author_id=2, title="Im tired of Dummy Posts", content=mkdx_content3),
        Post(author_id=2, title="Here lies another Dummy Post", content=mkdx_content4),
        Post(author_id=1, title="JUST STOP Loocking for moar Dummy Posts", content=mkdx_content2),
        Post(author_id=3, title="No comment, just  Dummy Posts", content=mkdx_content1)]
        # rellenamos la base de datos con un monton de Posts 12 x 15
        for x in posts:
            x.save()


    def handle(self, *args, **options):
        for x in range(15):
            self._create_posts()
        self._create_users()
