#Run with -H <hostname> parameters. This script assumes SSH key is in place

from fabric import task

@task
def apt_update(ctx):
    ctx.run('sudo apt-get update')

# @task
# def do_ping(ctx, hostname):
#     apt_update(ctx)
#     ctx.run(f'ping -c 3 {hostname}')

@task
def disable_swap(ctx):
    """ Disable swap because kubernetes doesn't support """
    ctx.sudo('sed -i "/ swap / s/^/#/" /etc/fstab')
    ctx.sudo('swapoff -a')
