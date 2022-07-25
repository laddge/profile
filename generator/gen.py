import os
import shutil
import toml
import jinja2


def load_icon(t, n):
    with open(os.path.join(os.path.dirname(__file__), f"icons/{t}/{n}.svg")) as f:
        return f.read().replace("fill=", "_fill=")


def gen():
    with open(os.path.join(os.path.dirname(__file__), "../config.toml")) as f:
        config = toml.load(f)
    with open(os.path.join(os.path.dirname(__file__), "template.html")) as f:
        tpl = jinja2.Template(f.read())
    config.update({"load_icon": load_icon})
    rendered = tpl.render(config)
    distdir = os.path.join(os.path.dirname(__file__), "../dist")
    if os.path.isfile(distdir):
        os.remove(distdir)
    if os.path.isdir(distdir):
        shutil.rmtree(distdir)
    shutil.copytree(os.path.join(os.path.dirname(__file__), "../assets"), distdir)
    with open(os.path.join(distdir, "index.html"), "w") as f:
        f.write(rendered)
    with open(os.path.join(distdir, "CNAME"), "w") as f:
        f.write(config["site"]["cname"])


if __name__ == "__main__":
    gen()
