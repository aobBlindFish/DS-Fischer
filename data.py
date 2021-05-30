from replit import db


def add_entry(value, key):
    if key in db:
        return False
    else:
        db[key] = value
        return True


def read_db(key=" "):

    key = str(key)
    content = []
    if key.isspace():
        for i in db.keys():
            content.append([i, db[i]])
    else:
        try:
            content.append(db[key])
        except KeyError:
            content = "nothing there"
    return content


def update_entry(value, key, change, value_change=False):
    def change_key(new_key):
        try:
            db[key]
            db[new_key] = value
            del db[key]
            return True
        except KeyError:
            return False

    def change_value(new_value):
        try:
            db[key]
            db[key] = new_value
            return True
        except KeyError:
            return False

    if value_change:
        return change_value(change)
    else:
        return change_key(change)


def delete_entry(key):
    try:
        del db[key]
        return True
    except KeyError:
        return False
