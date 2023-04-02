def cut_block(raw: str, start: str, stop: str = '\n\n') -> str:
    return raw.split(start, 1)[1].split(stop, 1)[0]


def extract(raw: str, pre: str, post: str, mid: str = None, mid_idx: int = 0, mid_rsplit: bool = False) -> str:
    ex1 = raw.split(pre, 1)[1].split(post, 1)[0]

    if mid is None:
        return ex1.strip()

    if mid_rsplit:
        return ex1.rsplit(mid, 1)[mid_idx].strip()

    return ex1.split(mid, 1)[mid_idx].strip()


def extract_post(raw: str, post: str, pre: str) -> str:
    return raw.split(post, 1)[0].rsplit(pre, 1)[1].strip()
