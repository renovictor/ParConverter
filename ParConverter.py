import re
import tkinter as tk
from tkinter import ttk, messagebox


# =============================================================================
# Conversion Engine
# =============================================================================

def normalize_value(val) -> str:
    """
    Normalize numeric strings:
    - hex 0x... -> int
    - floats like 1.00 -> 1
    - floats keep up to 6 decimals and trim trailing zeros
    - integers with leading zeros -> int string
    """
    if val is None:
        return ""

    s = str(val).strip()

    # Hex -> int
    if re.fullmatch(r"0x[0-9a-fA-F]+", s):
        return str(int(s, 16))

    # Try numeric normalization
    try:
        f = float(s)
        if f.is_integer():
            return str(int(f))
        return f"{f:.6f}".rstrip("0").rstrip(".")
    except Exception:
        # If it's integer-like with leading zeros
        if re.fullmatch(r"0+\d+", s):
            return str(int(s))
        return s


def parse_tlog_parameter_list(text: str) -> dict:
    """
    Parse text into a dict: {section_name: {param_id: raw_value_string}}
    Sections are recognized by lines starting with '//'
    Parameter pairs are parsed from comma-separated or whitespace-separated tokens.
    """
    section = None
    data = {}

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        # Section line
        if line.startswith("//"):
            section = line[2:].strip()
            data.setdefault(section, {})
            continue

        # Split by commas into chunks like "2 000000"
        parts = [p.strip() for p in line.split(",") if p.strip()]
        for p in parts:
            m = re.match(r"^(-?\d+)\s+(.+)$", p)
            if not m:
                continue
            pid = int(m.group(1))
            val = m.group(2).strip()
            data.setdefault(section or "Unknown", {})[pid] = val

    return data


# Output layout (order + header labels) exactly like user requested
SECTION_OUT_ORDER = [
    ("General\tParameters", "General Parameters", [
        2,3,4,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
        33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,
        63,64,65,66,67,68,69,70,71,72
    ]),
    ("Match\tParameters", "Match Parameters", [
        104,105,107,109,111,112,113,114,115,116,120,121,122,123,124,125,126,127,131,132,133,
        135,136,137,138,139,140,144,145,146,150,151,152,153,154,155,156,157,158,159,160,161,
        162,163,164,165,166,167,168,169
    ]),
    ("Generator\tParameters", "Generator Parameters", [
        300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,
        321,322,323,324,325,326,340,341,342,343,344,345,346,347,348,349,350,351
    ]),
    ("PIDs\t", "PIDs", [
        1,2,3,4,5,6,10,11,12,13,14,15,16,20,101,102,103,104,105,106,111,112,113,114,115,116,
        120,130,201,202,203,204,205,206,211,212,213,214,215,216,220,230,301,302,303,304,305,
        306,311,312,313,314,315,316,320,330
    ]),
]


def build_default_profile() -> dict:
    """
    Conversion profile:
    - ('src', src_id): take from input (v1.0.3: ALL parameters use this)
    - ('const', value): fixed value (REMOVED in v1.0.3 - no more hardcoded constants)
    - ('mul', src_id, factor): multiply numeric value

    v1.0.3 CHANGE: Profile now uses ONLY source-based rules.
    All parameters take their values directly from input data.
    This fixes issues where hardcoded constants were overriding input values.
    """
    profile = {
        "General Parameters": {},
        "Match Parameters": {},
        "Generator Parameters": {},
        "PIDs": {},
    }

    # --------------------------
    # General Parameters
    # --------------------------
    # v1.0.3: All parameters use input values (source-based), no hardcoded constants
    gen_src = [
        2,3,4,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,
        33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,
        63,64,65,66,67,68,69,70,71,72
    ]
    for oid in gen_src:
        profile["General Parameters"][oid] = ("src", oid)

    # --------------------------
    # Match Parameters
    # --------------------------
    # v1.0.3: All parameters use input values (source-based), no hardcoded constants
    match_src = [
        104,105,107,109,111,112,113,114,115,116,120,121,122,123,124,125,126,127,131,132,133,
        135,136,137,138,139,140,144,145,146,150,151,152,153,154,155,156,157,158,159,160,161,
        162,163,164,165,166,167,168,169
    ]
    for oid in match_src:
        profile["Match Parameters"][oid] = ("src", oid)


    # --------------------------
    # Generator Parameters
    # --------------------------
    # v1.0.3: All parameters use input values (source-based), no hardcoded constants
    genr_src = [
        300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,
        321,322,323,324,325,326,340,341,342,343,344,345,346,347,348,349,350,351
    ]
    for oid in genr_src:
        profile["Generator Parameters"][oid] = ("src", oid)


    # --------------------------
    # PIDs (mostly source-based per user requirement)
    # --------------------------
    # v1.0.3: All parameters use input values (source-based), no hardcoded constants
    pid_src = [
        1,2,3,4,5,6,10,11,12,13,14,15,16,20,101,102,103,104,105,106,111,112,113,114,115,116,
        120,130,201,202,203,204,205,206,211,212,213,214,215,216,220,230,301,302,303,304,305,
        306,311,312,313,314,315,316,320,330
    ]
    for oid in pid_src:
        profile["PIDs"][oid] = ("src", oid)

    return profile


DEFAULT_PROFILE = build_default_profile()


def compute_converted_text(parsed: dict, profile: dict) -> tuple[str, list[str]]:
    """
    Compute output text using SECTION_OUT_ORDER and profile.
    
    v1.0.2 BEHAVIOR (Fixed):
    - Parameters NOT in input are OMITTED from output (no hardcoded defaults)
    - Only parameters present in input are converted and outputted
    
    v1.0.1 feature (still active):
    - Automatically detects and appends unknown parameters (in input but not predefined)
    - Unknown parameters are sorted numerically and appended after predefined ones
    
    Returns: (output_text, warnings)
    """
    out_lines = []
    warnings = []

    for header, section_name, out_ids in SECTION_OUT_ORDER:
        out_lines.append(header)

        in_map = parsed.get(section_name, {})
        rules = profile.get(section_name, {})

        # Track which parameter IDs have been output
        output_ids_set = set(out_ids)

        # === PART 1: Output predefined parameters (maintains order) ===
        for oid in out_ids:
            # v1.0.2 FIX: Skip parameters NOT in input (don't output empty/constant values for missing params)
            if oid not in in_map:
                continue
            
            rule = rules.get(oid, ("src", oid))
            kind = rule[0]

            if kind == "src":
                src_id = rule[1]
                raw = in_map.get(src_id)
                if raw is None:
                    warnings.append(f"[{section_name}] Missing input param: {src_id} (needed for output {oid})")
                out_lines.append(f"{oid}\t{normalize_value(raw)}" if raw is not None else f"{oid}\t")

            elif kind == "const":
                out_lines.append(f"{oid}\t{normalize_value(rule[1])}")

            elif kind == "mul":
                src_id, factor = rule[1], rule[2]
                raw = in_map.get(src_id)
                if raw is None:
                    warnings.append(f"[{section_name}] Missing input param: {src_id} (needed for mul output {oid})")
                    out_lines.append(f"{oid}\t")
                else:
                    try:
                        v = float(raw)
                        out_lines.append(f"{oid}\t{normalize_value(v * factor)}")
                    except Exception:
                        warnings.append(f"[{section_name}] Non-numeric value for mul: {src_id}={raw}")
                        out_lines.append(f"{oid}\t")

            else:
                warnings.append(f"[{section_name}] Unknown rule type for {oid}: {rule}")
                out_lines.append(f"{oid}\t")

        # === PART 2: Detect and output unknown parameters (auto-detected) ===
        unknown_ids = sorted(set(in_map.keys()) - output_ids_set)
        
        for oid in unknown_ids:
            # Default rule: source mapping (use input value directly)
            rule = rules.get(oid, ("src", oid))
            kind = rule[0]

            if kind == "src":
                raw = in_map.get(oid)
                if raw is not None:
                    out_lines.append(f"{oid}\t{normalize_value(raw)}")
                else:
                    out_lines.append(f"{oid}\t")

            elif kind == "const":
                out_lines.append(f"{oid}\t{normalize_value(rule[1])}")

            elif kind == "mul":
                src_id, factor = rule[1], rule[2]
                raw = in_map.get(src_id)
                if raw is None:
                    out_lines.append(f"{oid}\t")
                else:
                    try:
                        v = float(raw)
                        out_lines.append(f"{oid}\t{normalize_value(v * factor)}")
                    except Exception:
                        out_lines.append(f"{oid}\t")

        out_lines.append("")  # blank line after each section

    return "\n".join(out_lines).rstrip() + "\n", warnings


# =============================================================================
# GUI
# =============================================================================

SAMPLE_INPUT_TEXT = """// General Parameters
2 000000, 3 00, 4 0, 6 1, 7 0, 8 0.0, 9 0, 10 0
11 0x6aa, 12 0x201, 14 0.0, 15 100.0, 16 5, 17 13, 18 20, 19 0
20 0, 21 000, 22 0, 23 25, 24 0, 25 20.00, 26 27.00, 27 100.0
28 98.0, 29 1500, 30 1320, 31 50, 32 2, 34 25, 35 1.0, 37 0
38 0, 39 4, 40 0, 50 50, 51 100, 52 1000, 53 5000, 54 100
55 1000, 56 5000, 57 100, 58 1000, 59 5000

// Match Parameters
104 5000.0, 105 1000.0, 107 0, 109 0, 111 650, 112 850, 113 650, 114 850
115 900, 116 1200, 120 0.0, 121 1.00, 122 0.00, 123 1.00, 124 0.00, 125 6
126 1.0, 127 13.560, 132 2, 133 60, 135 0, 136 0, 137 0, 138 0
139 12, 140 5, 144 15.0, 145 30, 146 0, 150 0, 151 2, 152 0.002
153 0.0, 154 0.0, 155 0, 156 0, 157 0, 158 0, 159 0.020, 160 0.005
161 0.60, 162 1.40, 163 1.80, 164 0.050, 165 0.070, 166 0.090, 167 3.00, 168 4.00
169 5.00

// Generator Parameters
300 1200, 301 -2.50, 302 0.90, 303 -2.33, 304 3000.0, 305 47.0, 306 100, 307 40.0
308 0.1, 309 5, 310 2, 311 2, 312 0, 313 0, 314 0, 315 3330.0
316 0, 317 1.00, 318 1, 319 50.0, 320 1, 321 0, 322 0, 323 0
324 5, 325 1, 340 50.0, 341 7.0, 342 550.0, 343 10.0, 344 550.0, 345 70.0
346 240.0, 347 2.0, 348 70.0, 349 50.0, 350 50.0, 351 180.0

// PIDs
1 1.000, 2 1.500, 3 0.000, 4 0.000, 5 -25.000, 6 25.000, 10 0.900
11 1.000, 12 5.000, 13 0.000, 14 0.000, 15 -50.000, 16 50.000, 20 1.100
101 1.000, 102 1.000, 103 0.000, 104 0.000, 105 -50.000, 106 50.000
111 1.000, 112 15.000, 113 0.000, 114 0.000, 115 -50.000, 116 50.000
120 0.000, 130 100.000
201 1.000, 202 2.000, 203 0.000, 204 0.000, 205 0.000, 206 0.000
211 1.000, 212 15.000, 213 0.000, 214 0.000, 215 0.000, 216 0.000
220 0.000, 230 10.000
301 1.000, 302 2.000, 303 0.000, 304 0.000, 305 0.000, 306 0.000
311 1.000, 312 15.000, 313 0.000, 314 0.000, 315 0.000, 316 0.000
320 0.000, 330 100.000
//
"""


class TlogConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tlog Parameter List Converter")
        self.geometry("1200x700")
        self.minsize(1050, 650)

        # --- Colors (dark + neon accents)
        self.bg = "#121826"          # dark navy
        self.panel = "#1A2235"       # card background
        self.panel2 = "#192B4A"      # alternate card
        self.fg = "#E6EEF8"
        self.muted = "#9FB3C8"
        self.accent = "#22C55E"      # green
        self.accent2 = "#60A5FA"     # blue
        self.warn = "#FBBF24"        # amber
        self.danger = "#F87171"      # red

        self.configure(bg=self.bg)

        self._setup_style()
        self._build_ui()

    def _setup_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("TFrame", background=self.bg)
        style.configure("Card.TFrame", background=self.panel, relief="flat")
        style.configure("Card2.TFrame", background=self.panel2, relief="flat")

        style.configure("Title.TLabel", background=self.bg, foreground=self.fg,
                        font=("Segoe UI", 18, "bold"))
        style.configure("Subtitle.TLabel", background=self.bg, foreground=self.muted,
                        font=("Segoe UI", 10))

        style.configure("CardTitle.TLabel", background=self.panel, foreground=self.fg,
                        font=("Segoe UI", 12, "bold"))
        style.configure("CardTitle2.TLabel", background=self.panel2, foreground=self.fg,
                        font=("Segoe UI", 12, "bold"))

        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"),
                        foreground="#0B1220", background=self.accent, padding=10)
        style.map("Accent.TButton",
                  background=[("active", "#34D399"), ("disabled", "#2F3A52")])

        style.configure("Blue.TButton", font=("Segoe UI", 10, "bold"),
                        foreground="#0B1220", background=self.accent2, padding=10)
        style.map("Blue.TButton",
                  background=[("active", "#93C5FD"), ("disabled", "#2F3A52")])

        style.configure("Ghost.TButton", font=("Segoe UI", 10),
                        foreground=self.fg, background="#2A3550", padding=10)
        style.map("Ghost.TButton",
                  background=[("active", "#354463"), ("disabled", "#2F3A52")])

        style.configure("Status.TLabel", background=self.bg, foreground=self.muted,
                        font=("Consolas", 10))

    def _build_ui(self):
        # Header
        header = ttk.Frame(self, style="TFrame")
        header.pack(fill="x", padx=16, pady=(14, 8))

        ttk.Label(header, text="Tlog Parameter List Converter", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header,
                  text="Paste tlog parameter list on the left → click Convert → get tab-separated result on the right.",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(2, 0))

        # Main area with two cards
        main = ttk.Frame(self, style="TFrame")
        main.pack(fill="both", expand=True, padx=16, pady=8)

        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(0, weight=1)

        # Left card (input)
        left = ttk.Frame(main, style="Card.TFrame")
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left.rowconfigure(1, weight=1)
        left.columnconfigure(0, weight=1)

        ttk.Label(left, text="Tlog Parameter List (Input)", style="CardTitle.TLabel")\
            .grid(row=0, column=0, sticky="w", padx=12, pady=(10, 6))

        self.input_text = tk.Text(left, wrap="none", height=10,
                                  bg="#0B1220", fg=self.fg, insertbackground=self.fg,
                                  font=("Consolas", 10),
                                  relief="flat", padx=10, pady=10)
        self.input_text.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))

        in_y = ttk.Scrollbar(left, orient="vertical", command=self.input_text.yview)
        in_x = ttk.Scrollbar(left, orient="horizontal", command=self.input_text.xview)
        self.input_text.configure(yscrollcommand=in_y.set, xscrollcommand=in_x.set)
        in_y.grid(row=1, column=1, sticky="ns", pady=(0, 12))
        in_x.grid(row=2, column=0, sticky="ew", padx=12)

        # Right card (output)
        right = ttk.Frame(main, style="Card2.TFrame")
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        right.rowconfigure(1, weight=1)
        right.columnconfigure(0, weight=1)

        ttk.Label(right, text="Converted Format (Output)", style="CardTitle2.TLabel")\
            .grid(row=0, column=0, sticky="w", padx=12, pady=(10, 6))

        self.output_text = tk.Text(right, wrap="none", height=10,
                                   bg="#071225", fg="#D8F3DC", insertbackground="#D8F3DC",
                                   font=("Consolas", 10),
                                   relief="flat", padx=10, pady=10)
        self.output_text.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))

        out_y = ttk.Scrollbar(right, orient="vertical", command=self.output_text.yview)
        out_x = ttk.Scrollbar(right, orient="horizontal", command=self.output_text.xview)
        self.output_text.configure(yscrollcommand=out_y.set, xscrollcommand=out_x.set)
        out_y.grid(row=1, column=1, sticky="ns", pady=(0, 12))
        out_x.grid(row=2, column=0, sticky="ew", padx=12)

        # Buttons row
        btn_bar = ttk.Frame(self, style="TFrame")
        btn_bar.pack(fill="x", padx=16, pady=(2, 10))

        ttk.Button(btn_bar, text="Insert Sample", style="Ghost.TButton", command=self.insert_sample).pack(side="left")
        ttk.Button(btn_bar, text="Clear", style="Ghost.TButton", command=self.clear_all).pack(side="left", padx=8)

        ttk.Button(btn_bar, text="Convert", style="Accent.TButton", command=self.convert).pack(side="right")
        ttk.Button(btn_bar, text="Copy Output", style="Blue.TButton", command=self.copy_output).pack(side="right", padx=8)

        # Status line
        self.status = tk.StringVar(value="Ready.")
        ttk.Label(self, textvariable=self.status, style="Status.TLabel")\
            .pack(fill="x", padx=16, pady=(0, 12))

    def insert_sample(self):
        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", SAMPLE_INPUT_TEXT)
        self.status.set("Sample inserted.")

    def clear_all(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.status.set("Cleared.")

    def copy_output(self):
        out = self.output_text.get("1.0", "end-1c")
        if not out.strip():
            self.status.set("Nothing to copy.")
            return
        self.clipboard_clear()
        self.clipboard_append(out)
        self.status.set("Output copied to clipboard.")

    def convert(self):
        raw = self.input_text.get("1.0", "end-1c").strip()
        if not raw:
            messagebox.showwarning("No input", "Please paste the tlog parameter list into the input box.")
            return

        try:
            parsed = parse_tlog_parameter_list(raw)
            converted, warnings = compute_converted_text(parsed, DEFAULT_PROFILE)

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", converted)

            # Status message with quick summary
            total_pairs = sum(len(v) for v in parsed.values())
            sec_names = [s for s in parsed.keys() if s]
            warn_count = len(warnings)

            if warn_count:
                self.status.set(f"Converted. Parsed {total_pairs} pairs in {len(sec_names)} sections. Warnings: {warn_count}")
            else:
                self.status.set(f"Converted. Parsed {total_pairs} pairs in {len(sec_names)} sections. No warnings.")

        except Exception as e:
            messagebox.showerror("Conversion failed", f"Error: {e}")
            self.status.set("Conversion failed.")


def main():
    app = TlogConverterApp()
    app.mainloop()


if __name__ == "__main__":
    main()
