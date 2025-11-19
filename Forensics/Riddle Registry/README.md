# Riddle Registry – picoCTF Writeup

## Challenge Summary

In this challenge, we were given a PDF named **confidential.pdf** along with a hint suggesting that the flag was hidden somewhere in the metadata. The PDF itself contained unreadable content, but its metadata turned out to be the key.

This writeup documents every step taken to safely inspect the file, uncover a suspicious Base64 string inside the *Author* field, decode it, and ultimately retrieve the flag.

---

## Why Metadata Matters

When investigating files, most people check the visible content or embedded media. However, **PDF metadata**—fields like *Author*, *Title*, *Keywords*, or the XMP block—can contain arbitrary text.

In CTFs, challenge creators frequently hide flags there because:

* It’s easy to overlook
* It doesn't require complex tools
* Metadata can store long text strings, including Base64

This challenge is a great reminder: **always check metadata.**

---

## Challenge: "Riddle Registry"

You're given a PDF that appears corrupted or nonsense, and the hint suggests the flag is hidden in its metadata. No steganography or reverse engineering required—just careful inspection.

---

## Step-by-Step Solution

### 1. Basic Inspection (Safety First)

Always work in a safe, isolated environment (VM or container). Never open unknown files directly.

Check file info and hash:

```bash
file confidential.pdf
ls -lh confidential.pdf
sha256sum confidential.pdf
```

This confirms it's a PDF and gives you the file hash for documentation.

---

### 2. Look for Visible Strings

Sometimes flags are directly embedded in the PDF text stream:

```bash
strings confidential.pdf | rg -n "picoCTF|picoCTF\{"
```

No useful results appeared, so we moved on to metadata inspection.

---

### 3. Inspect PDF Metadata

Using an online metadata viewer (or `exiftool` locally), we checked the **Author** field and found a suspicious Base64-like string:

```
cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=
```

The trailing `=` is often an indicator of Base64 encoding.

---

### 4. Decode the Base64

You can use base64Decoder.py or decoded it using a terminal command:

```bash
echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=' | base64 --decode
```

**Result:**

Decoded text:
```
 picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}
```

And that was the flag.

---

## Final Flag

**`picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}`**

---

## Takeaway

This challenge reinforces an important principle in digital forensics and CTFs:

> **Always inspect metadata. Hidden data often lives where no one thinks to look.**

Simple tools and careful observation can reveal everything you need.

---
