# Limits from BIS IS 10500:2012 (Indian drinking-water standard).
# "max" is the acceptable limit. "max_permissible" is the highest value allowed
# when no alternate source exists; None means the standard allows no relaxation.
# Only include parameters your strip actually measures.
limits = {
    "pH":             {"unit": "",     "min": 6.5, "max": 8.5, "max_permissible": None},
    "Turbidity":      {"unit": "NTU",  "max": 1,    "max_permissible": 5},
    "Total hardness": {"unit": "mg/L", "max": 200,  "max_permissible": 600},
    "Alkalinity":     {"unit": "mg/L", "max": 200,  "max_permissible": 600},
    "Nitrate":        {"unit": "mg/L", "max": 45,   "max_permissible": None},
    # Chlorine: 0.2 is a minimum residual for treated supplies. Untreated water
    # has none, which is normal, so low values are not flagged.
    "Free chlorine":  {"unit": "mg/L", "min": 0.2, "max": 1.0, "max_permissible": None, "low_is_ok": True},
}


def classify(name: str, value: float) -> dict:
    rule = limits [name]
    lo, hi, hi_perm = rule.get("min"), rule.get("max"), rule.get("max_permissible")
    status = "normal"

    if lo is not None and value < lo and not rule.get("low_is_ok"):
        status = "caution"
    if hi is not None and value > hi:
        # "danger" only when beyond the permissible limit. Strips are coarse,
        # so anything else outside the acceptable range is "caution".
        status = "danger" if (hi_perm is not None and value > hi_perm) else "caution"

    unit = f" {rule['unit']}" if rule["unit"] else ""
    return {"name": name, "value": f"{value}{unit}", "status": status}