./blender ../benchmark.blend --background --python ../blend.py

Example command
To render a single frame (using GPU(s)) from a blendfile.blend file located in /source/path on the docker host and save the result in the same directory. Make sure the force_gpu.py script is available as well!

docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all --rm -v /source/path:/media vogete/blender-cuda /media/blendfil

Multi GPU
docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all --rm --entrypoint "" vogete/blender-cuda nvidia-smi
