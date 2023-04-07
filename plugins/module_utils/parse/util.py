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


def extract_debug(p: dict, r: dict, raw: str) -> str:
    if p['debug']:
        data = []

        if 'debug' not in r:
            r['debug'] = []

        for idx, line in enumerate(raw.splitlines()):
            if idx == 0:
                # date + time
                r['debug'].append(line)
                continue

            if line.startswith('DEBUG: '):
                r['debug'].append(line)

            else:
                data.append(line)

        return '\n'.join(data)

    return raw
