from fabric.context_managers import shell_env
from fabric.operations import sudo
from offregister_fab_utils.apt import apt_depends


def install0(SERVER_NAME, *args, **kwargs):
    apt_depends("curl", "openssh-server", "ca-certificates")
    apt_depends("postfix")

    external_url = "{protocol}://{server_name}".format(
        protocol=kwargs.get("https") or "http", server_name=SERVER_NAME
    )
    sudo(
        "curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | bash"
    )
    with shell_env(EXTERNAL_URL=external_url):
        apt_depends("gitlab-ee")
