class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = "bQeThWmZq4t7w!z$C&F)J@NcRfUjXn2r"

    DB_NAME = "production-db"
    DB_HOST = "gvzimvfsr50s.aws-sa-east-1-1.psdb.cloud"    
    DB_USERNAME = "pdpgox29gca3"
    DB_PASSWORD = "pscale_pw_loLKuCwDoakA9zakAV4nFMVqqnbxD1o7bqgsiHoX-J0"
    DB_SERVICE = "dev"

    OCI_USER = "ocid1.user.oc1..aaaaaaaauwrtap76ljaeoc2z3qxpzm6zhgzwc4fvxgisatsiskpjzfkfb2uq"
    OCI_FP = "96:e8:3c:9c:a6:11:7d:ef:db:97:45:a0:ac:65:49:c5"
    OCI_TENANCY = "ocid1.tenancy.oc1..aaaaaaaaqw7dujkyfeh4mpbj35n26znrrfvk6i7exlrbflhkmrih3w5jdlsq"
    OCI_REGION = "sa-santiago-1"
    OCI_KF = "/.oci/dataminds.api_2022-06-16T16_18_13.047Z.pem"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True