import os

def create_directory_structure():
    # Répertoires principaux
    main_directories = ['src', 'public']

    for directory in main_directories:
        os.makedirs(directory)
        print(f'Dossier créé : {directory}')

    # Répertoires dans 'src'
    src_directories = ['controllers', 'models', 'views', 'database']

    for directory in src_directories:
        os.makedirs(os.path.join('src', directory))
        print(f'Dossier créé : src/{directory}')

    # Fichiers dans 'src'
    src_files = ['SchoolController.js', 'AccountingController.js', 'DonationController.js',
                 'School.js', 'Student.js', 'Teacher.js', 'Donation.js', 'Transaction.js',
                 'SchoolView.js', 'AccountingView.js', 'DonationView.js',
                 'DatabaseConfig.js', 'SchoolDatabase.js', 'AccountingDatabase.js', 'DonationDatabase.js']

    for file in src_files:
        with open(os.path.join('src', file), 'w') as f:
            f.write('')
        print(f'Fichier créé : src/{file}')

    # Fichiers dans 'public'
    public_files = ['index.html', 'app.js', 'package.json', 'README.md']

    for file in public_files:
        with open(file, 'w') as f:
            f.write('')
        print(f'Fichier créé : {file}')

if __name__ == "__main__":
    create_directory_structure()
