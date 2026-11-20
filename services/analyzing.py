def split_dataset(X, y):
    """
    Split a dataset into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def display_image(image):
    """
    Display an image using Matplotlib.
    """
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.show()


def prepare_image(sample, width=28, height=28):
    """
    Convert a flattened numerical sample into an image.
    """
    image = np.asarray(sample)

    if image.size != width * height:
        raise ValueError(
            f"Expected {width * height} values, got {image.size}."
        )

    return image.reshape(height, width)


