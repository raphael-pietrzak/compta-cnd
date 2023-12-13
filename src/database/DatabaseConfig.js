// DatabaseConfig.js
const mongoose = require('mongoose');

class DatabaseConfig {
    static connect() {
        const dbUri = 'mongodb://localhost:27017/your_database_name';

        mongoose.connect(dbUri, { useNewUrlParser: true, useUnifiedTopology: true })
            .then(() => {
                console.log('Connected to the database');
            })
            .catch((err) => {
                console.error('Error connecting to the database:', err);
            });

        mongoose.connection.on('error', (err) => {
            console.error('MongoDB connection error:', err);
        });
    }
}

module.exports = DatabaseConfig;


