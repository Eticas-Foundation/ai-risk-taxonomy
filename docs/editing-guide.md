# How to edit the Eticas AI Risk Taxonomy

This guide walks you through adding or editing risk categories and subcategories. You don't need to install anything — everything is done through the GitHub website.

The key safety feature: **you never edit the live version directly.** You make changes on a copy (a "branch"), the system checks your changes automatically, and someone reviews before they go live. If you make a mistake, nothing breaks.

---

## Before you start

You need a GitHub account that is a member of the Eticas-Foundation organisation. If you can see `https://github.com/Eticas-Foundation/ai-risk-taxonomy`, you're set.

---

## Adding a new subcategory

This is the most common task — for example, adding a new type of risk under an existing category.

### Step 1: Open the taxonomy file

Go to: `https://github.com/Eticas-Foundation/ai-risk-taxonomy/blob/main/src/taxonomy.yaml`

Click the **pencil icon** (top right of the file view) to edit.

GitHub will show a message saying *"You're making changes in a project you don't have write access to"* or *"You need to fork/create a branch"*. This is normal — it's creating your personal copy to work on.

### Step 2: Find where to add your entry

Scroll through the file to find the category your subcategory belongs under. Categories are marked with comments like:

```
# ============================================================
# 1. BIAS & FAIRNESS
# ============================================================
```

Find the last subcategory under that category. You'll add your new entry after it.

### Step 3: Copy and fill in this template

Copy the block below and paste it after the last subcategory in the relevant category. Replace everything in CAPS with your content:

```yaml
  - id: YOUR-ID-HERE
    type: subcategory
    broader: PARENT-CATEGORY-ID
    label: "YOUR LABEL HERE"
    definition: >
      YOUR DEFINITION HERE. This can be multiple sentences.
      Keep the indentation (6 spaces before the text).
    scope: ALL
    lifecycle_stages: [post-processing]
```

**Rules for filling this in:**

| Field | What to write | Example |
|-------|--------------|---------|
| `id` | A short identifier using lowercase letters and hyphens. No spaces. | `automation-bias` |
| `broader` | The `id` of the parent category. Copy it exactly. | `bias-fairness` |
| `label` | The human-readable name, in quotes. | `"Automation bias"` |
| `definition` | A clear description. Start with `>` then write on the next line, indented 6 spaces. | (see template) |
| `scope` | `ALL` (both ADM and LLM), `ADM` (only ADM), or `LLM` (only LLM). | `ALL` |
| `lifecycle_stages` | Which stages this applies to. Use square brackets. | `[pre-processing, post-processing]` |

**Valid values for lifecycle_stages:** `pre-processing`, `in-processing`, `post-processing`

**Valid parent category ids:** `bias-fairness`, `privacy-confidentiality`, `reliability`, `governance`, `security-misuse`, `environmental-impact`, `transparency-explainability`, `responsibility-redress`, `autonomy`, `agentic-risks`, `manipulation-misinformation`

### Step 4: Commit your change

Scroll down. You'll see a "Commit changes" section:

1. In the commit message box, write a short description like: `Add automation-bias subcategory under Bias & Fairness`
2. Select **"Create a new branch for this commit and start a pull request"**
3. Leave the branch name as suggested (or change it to something descriptive)
4. Click **"Propose changes"**

### Step 5: Open the pull request

GitHub takes you to a "Open a pull request" page. Add any notes about why you're adding this subcategory, then click **"Create pull request"**.

### Step 6: Wait for the check

Within about 30 seconds, you'll see a status check appear on the pull request:

- **Green check ✓** — Your YAML is valid. Ask a colleague to review and merge.
- **Red X ✗** — Something is wrong. Click "Details" to see the error message. It will tell you exactly what's wrong in plain language, like: `"automation-bias": Missing required field "definition"` or `"automation-bias": Invalid scope "adm". Must be "ALL", "ADM", or "LLM".`

If you see an error, click the pencil icon on the pull request's "Files changed" tab to edit and fix it. The check runs again automatically.

### Step 7: Merge

Once the check passes and a colleague approves, click **"Merge pull request"** and then **"Confirm merge"**. The system automatically regenerates all the pages.

---

## Adding a new category

This is less common — it means adding a top-level risk area, not just a subcategory.

Use this template, placed after the last category block in the file:

```yaml
  # ============================================================
  # NEW CATEGORY NAME
  # ============================================================

  - id: your-category-id
    type: category
    label: "Your Category Name"
    alt_labels:
      - "Alternative name if any"
    definition: >
      Your definition here. Describe the risk area clearly.
      This can be multiple sentences.
    scope: ALL
    lifecycle_stages: [pre-processing, in-processing, post-processing]
    inclusion: audit-dependent
    maturity: provisional
    mappings:
      - framework: mit
        target_id: "subdomain-X.X"
        target_label: "MIT equivalent concept"
        relation: closeMatch
```

**Notes:**
- New categories should almost always start as `inclusion: audit-dependent` and `maturity: provisional`. They can be promoted later.
- The `mappings` section is optional — you can add it later or ask a colleague to fill it in.
- The `alt_labels` section is optional — include it only if the category is known by other names.

The commit and review process is the same as for subcategories (steps 4–7 above).

---

## Editing an existing entry

1. Open `src/taxonomy.yaml` on GitHub
2. Click the pencil icon
3. Find the entry you want to change
4. Make your edit
5. Follow steps 4–7 above (commit on a branch, open PR, wait for check, merge)

Common edits:
- **Changing a definition:** Edit the text after `definition: >`. Keep the indentation.
- **Adding an alternative label:** Add a line under `alt_labels:` with a dash and the new name: `- "New Name"`
- **Changing scope:** Replace `ALL` with `ADM` or `LLM` (or vice versa).
- **Adding a lifecycle stage:** Add it inside the square brackets, e.g., `[pre-processing, post-processing]`

---

## Common mistakes and how to fix them

**"YAML syntax error at line X"**
Usually means incorrect indentation. Every level of indentation must use exactly 2 spaces (not tabs). Make sure your new entry aligns with the entries above and below it.

**"Missing required field"**
You forgot one of the required fields (id, type, label, definition). Add it.

**"Duplicate id"**
The id you chose already exists in the file. Pick a different one.

**"broader does not match any id"**
The parent category id has a typo. Check the list of valid category ids above.

**"Invalid scope / inclusion / maturity"**
You used a value that isn't in the allowed list. Check the valid values listed above.

---

## The golden rules

1. **Always work on a branch, never edit main directly.** GitHub's "Propose changes" flow does this for you automatically.
2. **Use the templates above.** Copy-paste and replace — don't write from scratch.
3. **Watch the indentation.** Every line in an entry starts with exactly 4 spaces. Sub-items (like mappings) start with 6 or 8 spaces. When in doubt, copy the indentation from the entry above yours.
4. **Wrap labels in quotes.** Always write `label: "Your Label"` with the double quotes.
5. **Check the green/red status** on your pull request before asking someone to merge.

---

## Quick reference: file structure

Each entry in the file looks like this:

```yaml
··- id: example-id                          ← unique identifier (lowercase, hyphens)
····type: subcategory                       ← "category" or "subcategory"
····broader: parent-id                      ← parent category id (subcategories only)
····label: "Example Label"                  ← display name (in quotes)
····definition: >                           ← description (> means multi-line)
······Your definition text here.
······Continue on the next line at the same indentation.
····scope: ALL                              ← ALL, ADM, or LLM
····lifecycle_stages: [post-processing]     ← list in square brackets
```

(The dots `··` represent spaces — 2 spaces per level of indentation.)
