def pred_eq_len(length):
    return lambda x: len(x) == length


def pred_ne_len(length):
    return lambda x: len(x) != length


def pred_le_length(length):
    return lambda x: len(x) <= length


def pred_ge_length(length):
    return lambda x: len(x) >= length


def pred_lt_length(length):
    return lambda x: len(x) < length


def pred_gt_length(length):
    return lambda x: len(x) > length


def pred_eq(value_to_match):
    return lambda x: x is value_to_match or x == value_to_match


def pred_eq_ref(value_to_match):
    return lambda x: x is value_to_match


def pred_contains(value_to_contain):
    return lambda x: value_to_contain in x


def pred_contains_eq_count(*values_to_contain, count=None):
    count = count if count is not None else len(values_to_contain)
    return lambda x: sum(1 for v in values_to_contain if v in x) == count


def pred_contains_all(*values_to_contain):
    return lambda x: all(v in x for v in values_to_contain)


def combine_preds(*preds):
    return lambda x: all(pred(x) for pred in preds)
