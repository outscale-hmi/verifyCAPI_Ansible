# ansible-workflow-k8s

## Cluster API Outscale CI/CD

This repository provides a CI/CD pipeline for testing the Cluster API Outscale Helm chart.

## Prerequisites
- Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- Install [helm](https://github.com/helm/helm/releases)
- Outscale account with [Access Key and Secret Key](https://wiki.outscale.net/display/EN/Creating+an+Access+Key)
- A Kubernetes cluster:
  - Local Kubernetes clusters with [kind](https://github.com/kubernetes-sigs/kind#installation-and-usage)
  - Remote clusters using [osc-rke](https://github.com/outscale-dev/osc-k8s-rke-cluster)

## Deployment Steps
1. Deploy the Cluster API Outscale Helm chart:
   ```bash
   aansible-playbook -i inventory/hosts.ini playbooks/deploy.yml

2. Validate the deployment:
  ```bash
 ansible-playbook -i inventory/hosts.ini playbooks/validate.yml
  ```
3.Cleanup resources:
  ```bash
  ansible-playbook -i inventory/hosts.ini playbooks/cleanup.yml
  ```

---

## **Key Features**
1. **Automation**: Ansible playbooks manage deployment, validation, and cleanup.
2. **Reusability**: Playbooks can be run locally or in CI/CD pipelines.
3. **Modularity**: Each task (e.g., deployment, validation, cleanup) is isolated for easy debugging.

With this setup, your CI/CD pipeline will handle deploying, validating, and cleaning up the Cluster API Outscale Helm chart efficiently.






