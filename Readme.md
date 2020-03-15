The benchmark.blend file is tracked using git LFS

Build Docker image:
`docker build -t shawn/blender_docker .`

Run Docker image on select GPUs:
`docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0,1 --rm -it shawn/blender_docker sh`

Run Docker image on all GPUs:
`docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all --rm -it shawn/blender_docker sh`

Once container is up and running:

    cd blender_install
    ./blender ../benchmark.blend --background --python ../blend.py

