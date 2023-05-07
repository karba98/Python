module.exports = {
  apps: [{
    name: 'py_api',
    script: 'uvicorn',
    args: 'api:app --reload --port 3555 --host 0.0.0.0',
    cwd: '/var/www/Python/py_api/app',
    interpreter: '/usr/bin/python3',
    watch: true,
    env: {
      PYTHONUNBUFFERED: 1,
      PYTHONIOENCODING: 'UTF-8',
      LC_ALL: 'en_US.UTF-8',
      LANG: 'en_US.UTF-8'
    }
  }]
};
