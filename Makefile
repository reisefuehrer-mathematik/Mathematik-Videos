VERBOSE = @
MANIM = python3 -m manim

out/videos/%.mp4:
	$(VERBOSE) $(MANIM) videos/$*.py $(*F) -pqh -c manim.cfg --custom_folders

example: out/videos/example/Example.mp4

.PHONY: example