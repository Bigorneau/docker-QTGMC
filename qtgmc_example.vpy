import vapoursynth as vs
import havsfunc as haf

# Initialize VapourSynth Core
core = vs.core

# 1. Load the video source
# Ensure the plugin (e.g., ffms2 or lsmas) is installed
clip = core.ffms2.Source(source="input_interlaced.mkv")

# 2. Set Field Order
# QTGMC needs to know if the clip is Top Field First (TFF) or Bottom Field First (BFF)
# If not set in metadata, you can force it:
# clip = core.std.SetFrameProp(clip, prop="_FieldBased", intval=2) # 2=TFF, 1=BFF

# 3. Apply QTGMC
# Presets: 'Placebo', 'Very Slow', 'Slower', 'Slow', 'Medium', 'Fast', 'Faster', 'Very Fast', 'Super Fast', 'Ultra Fast', 'Draft'
# TFF: Top Field First (True for most HD content)
clip = haf.QTGMC(clip, Preset='Slower', TFF=True)

# 4. Set Output
clip.set_output()
