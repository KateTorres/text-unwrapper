# utils/operation_menu.py
def choose_operation() -> str:
    print("\nSelect processing mode:")
    print("  1) Unwrap paragraphs only")
    print("  2) Remove numeric [n] brackets only")
    print("  3) Both 1 and 2")
    choice = input("Enter 1 / 2 / 3 (default 3): ").strip() or "3"
    return {"1": "unwrap",
            "2": "remove_refs",
            "3": "both"}.get(choice, "both")
