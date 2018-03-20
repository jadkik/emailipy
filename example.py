import emailipy

src = {}

for extension in ["html", "css"]:
    with open("tests/test.{}".format(extension), "r") as f:
        src[extension] = f.read()

def header(text):
    print("\n", text, "\n", "=" * len(text))

header("Original CSS")
print(src["css"])

header("Original HTML")
print(src["html"])

header("Results of CSS Linting")
for violation in emailipy.lint_css(src["css"]):
    print(violation)

header("HTML w/ inlined CSS")
print(emailipy.inline_css(*list(src.values())))