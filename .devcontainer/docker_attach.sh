DIRECTORY_NAME="chicken-tinder"

docker container run \
    -it \
    --rm \
    --name chickentinder.info.image.container \
    --user vscode \
    --mount type=bind,source=/home/ubuntu/Projects/$DIRECTORY_NAME,target=/workspace/$DIRECTORY_NAME \
    --workdir /workspace/$DIRECTORY_NAME \
    --publish 7777:7777 \
    chickentinder.info.image /bin/bash && pip3 install -r requirments.txt
