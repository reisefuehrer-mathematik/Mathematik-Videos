VERBOSE = @
MANIM = python3 -m manim

out/videos/%.mp4:
	$(VERBOSE) $(MANIM) videos/$*.py $(*F) -pqh -c manim.cfg --custom_folders