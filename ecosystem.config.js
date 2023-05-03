module.exports = {
  apps : [{
    name: 'i_have_been_pwned-python',
    cmd: './app/main.py',
    autorestart: true,
    watch: true,
    instances: 4,
    interpreter: './app/venv/Scripts/python.exe',
    max_memory_restart: '1G',
    env: {
      ENV: 'development'
    },
    env_production : {
      ENV: 'production'
    }
  }]
};