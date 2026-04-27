# VapourSynth Scripting & Plugin Guide

VapourSynth operates using three main components: the **Core Library**, **Binary Plugins**, and **Python Scripts**.

## 1. Binary Plugins (.so)
Plugins are compiled C/C++ libraries that provide high-performance filters. 
- **Standard Path:** `/usr/lib/vapoursynth/` (on Linux) or defined by `VS_PLUGIN_PATH`.
- **Loading:** VapourSynth automatically loads plugins from the standard path. To load a plugin from a custom location:
  ```python
  core.std.LoadPlugin(path="/path/to/plugin.so")
  ```
- **Usage:** Plugins are accessed via namespaces (e.g., `core.mv.Analyse`, `core.std.Transpose`).

## 2. Python Scripts (.py)
Scripts are high-level wrappers or complex functions (like QTGMC) written in Python.
- **Location:** Scripts must be in your Python module search path.
- **Paths:** Place scripts in `/usr/lib/python3/dist-packages/` or add a custom folder to your `PYTHONPATH` environment variable.
- **Usage:** Standard Python imports (e.g., `import havsfunc as haf`).

## 3. QTGMC Requirements
To use the QTGMC deinterlacer via `havsfunc`, the following must be installed:

### Plugins
- **MVTools:** Motion estimation and compensation.
- **RgTools:** RemoveGrain and Repair filters.
- **MaskTools2:** Masking and merging operations.
- **znedi3 / nnedi3cl:** Intra-field interpolation.
- **fmtconv:** Bit-depth and color space conversions.

### Scripts
- **havsfunc.py:** Contains the `QTGMC` function.
- **mvsfunc.py:** General helper functions.

---

## Running Scripts
Use `vspipe` to output or encode:
```bash
vspipe -c y4m script.vpy - | ffmpeg -i - -c:v libx264 -crf 18 output.mp4
```
