from packageLoader import load_packages_from_csv, print_all_packages


def main():
    csv_file_path = 'WGUPS Package File.csv'
    package_list = load_packages_from_csv(csv_file_path)
    print_all_packages(package_list)

if __name__ == "__main__":
    main()