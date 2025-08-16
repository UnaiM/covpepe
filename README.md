covpepe
=======

**Copy files/folders as “safe” text.**

Since it uses [Base85] encoding, where every character is printable and non-special, the resulting text in your clipboard shouldn’t fall victim of any substitution or omission, like the ones that chat, email or word processing applications introduce.

Also (the original use-case), remote connection software might garble data when copying across different OSs, so this eliminates that.


Requirements
------------

* [Python] 3.6 or higher
* [Pyperclip] (handled by installation script, see below)


Installation
------------

Simply open this repo’s `install` folder, and run the appropriate executable for your OS. `*_install` will do the following:

1. Create a Python virtual environment
2. Install Pyperclip in that virtual environment
3. Register right-click menu actions for files/folders **(WIP: Windows only.)**

`*_uninst` will undo the above.


Usage
-----

Once installed, if you select one or more files/folders in your OS, right-clicking on them should show a _covpepe_ option.[^1][^2] **(WIP: Windows only.)** This will store a copy of the contents of the files/folders you’ve selected, ready to be “pasted” elsewhere as explained right below.

Right-clicking on an empty space next to where files/folders are listed, you should also get a _pasvtete_ option.[^2] **(WIP: Windows only.)** This will re-create the files/folders you “copied” above, in the directory where you right-clicked.


### Command-line usage

`covpepe` and `pasvtete` are also commands, under this repo’s `bin` folder. Run them followed by a space and `--help` to get more info.


Why that name?
--------------

It’s a combination of the word ‘copy’ (and ‘paste’ in the case of _pasvtete),_ and the [‘covfefe’ meme]. I’m not affiliated with Donald Trump; I just think it’s fuvnene (funny).

Incidentally, I always thought ‘covfefe’ meant ‘coffee’— this might explain why things like ‘covpepe’ and ‘fuvnene’ make sense in my brain (‘pasvtete’ is a stretch).


[^1]: On Windows, this is under the _Send to_ submenu.
[^2]: On Windows 11, either Shift + right-click, or upon normally right-clicking, choose _Show more options._

[Base85]: https://en.wikipedia.org/wiki/Ascii85 'Ascii85 - Wikipedia'
[Python]: https://python.org 'Welcome to Python.org'
[Pyperclip]: https://github.com/asweigart/pyperclip 'asweigart/pyperclip: Python module for cross-platform clipboard functions.'
[‘covfefe’ meme]: https://en.wikipedia.org/wiki/Covfefe 'Covfefe - Wikipedia'
