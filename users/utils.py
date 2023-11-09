import pandas as pd

from .models import CategoryModel, UserModel


def create_user_instance(row):
    """
    Function for create instance of User model
    """
    return UserModel(
        first_name=row["firstname"],
        last_name=row["lastname"],
        email=row["email"],
        gender=row["gender"],
        birth_date=row["birthDate"],
        category=row["category"],
    )


def import_data_from_csv(file_path: str):
    # Upload data to DataFrame
    df = pd.read_csv(file_path)

    # Get unique categories from file
    unique_categories = df["category"].unique()
    category_mapping = {
        category: CategoryModel.objects.get_or_create(name=category)[0]
        for category in unique_categories
    }

    # Transform data
    df["category_id"] = df["category"].map(category_mapping)
    df["category"] = df["category_id"]
    df.drop(columns=["category_id"], inplace=True)
    df["gender"].replace({"male": "M", "female": "F"}, inplace=True)

    # Create Users
    user_instances = df.apply(create_user_instance, axis=1).tolist()
    UserModel.objects.bulk_create(user_instances)

    return "Data was created!"
