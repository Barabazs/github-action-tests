#!/bin/env bash

LABEL_NAME=$(jq --raw-output '.label.name' "$GITHUB_EVENT_PATH")
if [[ "$LABEL_NAME" == "major" || "$LABEL_NAME" == "minor" || "$LABEL_NAME" == "patch" ]]; then
    label=$LABEL_NAME

    api_version=$(git describe --abbrev=0 --tags)
    IFS='.' read -a version_split <<<"${api_version}"
    current_major=${version_split[0]}
    current_minor=${version_split[1]}
    current_patch=${version_split[2]}
    if [[ $label = "major" ]]; then
        current_major=$(echo "$current_major + 1" | tr -d $'\r' | bc)
        current_minor=0
        current_patch=0
    elif [[ $label = "minor" ]]; then
        current_minor=$(echo "$current_minor + 1" | tr -d $'\r' | bc)
        current_patch=0
    elif [[ $label = "patch" ]]; then
        current_patch=$(echo "$current_patch + 1" | tr -d $'\r' | bc)
    fi
    new_version="${current_major}.${current_minor}.$current_patch"
    echo "Bumping packaging patch version from $api_version to $new_version"
fi
