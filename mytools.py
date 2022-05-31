
from pattern.text.en import parse, Sentence


@staticmethod
def Analyze(txt) :
    parsed = parse(txt)
    result = Sentence(parsed)
    cmd = ""
    for ch in result.chunk:
        cmd += ch.string+" "

    return cmd


@staticmethod
def log(*vals):
    print(vals)


# @staticmethod
# def SpacyAnalze() :
