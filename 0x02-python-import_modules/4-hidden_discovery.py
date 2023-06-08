#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
hidden_names = dir(hidden_4)
for hidden_name in hidden_names:
    if not hidden_name.startswith("__"):
        print(hidden_name)
