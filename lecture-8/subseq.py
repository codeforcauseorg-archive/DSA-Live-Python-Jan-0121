def subseq(unproc, proc=""):
    if unproc == "":
        print(proc)
        return

    ch = unproc[0]

    subseq(unproc[1:], proc + ch)
    subseq(unproc[1:], proc)

subseq("abc")