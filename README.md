# Aleph Whiteper

You can see the last build of the [WhitePaper PDF in this repository](aleph-whitepaper.pdf). Keep in mind it is still a work in progress, and any information found here is subject to change, supply and token distribution included.

Before making, install linked tools:

```
$ npm install mermaid.cli
$ pip3 install -r requirements.txt
```

Then run "make" command to generate the pdf file.

On ubuntu you might need to install packages with that command:

```
sudo apt install texlive-latex-extra texlive-latex-recommended pandoc pandoc-citeproc texlive-extra-utils texlive texlive-lang-english python3-pandocfilters python3-tk texlive-fonts-extra texlive-fonts-recommended texlive-xetex
```

You might also need to do this:
```
export PATH=$PATH:~/.local/bin
```

Now, just build:
```
make
```