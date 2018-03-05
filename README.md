# vs<sup>3</sup>

vktec's simple site system.

## What?

vs<sup>3</sup> is the spiritual successor to [vsg][vsg], my super simple
static site generator written in Python. vs<sup>3</sup> aims to be even
more simple, but also more powerful because it supports dynamic content.

[vsg]: https://github.com/vktec/vsg

## Usage

vs<sup>3</sup> is written in Bash, and its templating is based on Bash.
However, you do not need to know how to use Bash to use vs<sup>3</sup>.
Here's a sample vs<sup>3</sup> template:

    <!DOCTYPE html>
    <title>
    $> e "$title"
    |
    $> e "$site_name"
    </title>
    $> echo "$content"

This template creates a simple HTML page with a `<title>` element
containing the HTML-escaped page name and site title. In the body of
the resulting HTML, it places the non-escaped content of the page.

Pages are written in Markdown (with a few extra bits; see below), and
might look something like this:

    $$$
    title='My page title'
    $$$
    # Hello, world!

    This is a **Markdown** page.

The block with `$$$` on either side is interpreted directly, as Bash code.
This allows you to set variables that affect the template. You can also
use the same syntax as in templates (`$> code`) to inject the output of
commands into your page as Markdown.

## How?

vs<sup>3</sup> works by transforming templates and source files into Bash
scripts, which it then runs to generate page content. This transformation
is done automatically (ie. there is no "build" step), but the results
are cached so that it is only performed when the source files are updated.

vs<sup>3</sup> is not a CGI script, but it is designed to be easy to use
from one. It outputs the rendered page to `stdout` and accepts command
line arguments as normal. Because arbitrary bash code can be run in pages
and templates, you could even use CGI environment variables from within
them to create a truly dynamic website with vs<sup>3</sup>.

## Dependencies

vs<sup>3</sup> does not have many dependencies. It should run with most
versions of Bash (though see the security notes below), and its only other
dependency is the [`markdown`][md] command. If you want to use a different
Markdown implementation with a different command name, modify the source
code (don't worry, it's a tiny program).

[md]: https://daringfireball.net/projects/markdown/

## Security notes

The HTML escaping provided by vs<sup>3</sup> is not perfect. It's not even
close to perfect. [HTML escaping is hard][escaping], and I've not tried
to do it perfectly. Context is crucial, but here are some rules of thumb:

- `e` should be fine for the content of HTML tags (except `<script>` and
  `<style>` tags which are special and you shouldn't be using
  user-generated content in anyway).
- Always use `attr` for setting attributes of HTML tags dynamically.
  `attr` basically just uses `e` with double quotes, but you shouldn't
  do that manually in case a security flaw comes up and I change `attr`
  to patch it.
- Beware of command injection. If you're doing a variable expansion into
  a Bash command, quote it.
- Context matters. If in doubt, consult the source code.

Also, vs<sup>3</sup> is written in Bash, for which there have been
vulnerabilities in the past (ShellShock). Please ensure you are running an
up-to-date version of Bash.

[escaping]: https://wonko.com/post/html-escaping
