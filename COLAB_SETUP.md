# Google Colab Auto-Deployment Setup Guide

This guide will help you set up automatic deployment of your Pokemon Showdown Gym repository to Google Colab.

## 🚀 Quick Start

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UoA-CARES/showdown_gym/blob/main/colab_setup.ipynb)

Click the badge above to open this repository directly in Google Colab!

## 📋 Prerequisites

- GitHub repository with your Pokemon Showdown Gym code
- Google account for Colab access
- Basic understanding of Git and GitHub

## 🛠️ Setup Instructions

### 1. Repository Structure

Ensure your repository has the following structure:

```
showdown_gym/
├── .github/
│   └── workflows/
│       └── colab-deployment.yml
├── showdown_gym/
│   ├── __init__.py
│   ├── base_environment.py
│   └── showdown_environment.py
├── colab_setup.ipynb
├── colab_environment.py
├── requirements-colab.txt
├── requirements.txt
├── setup.py
└── README.md
```

### 2. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Enable GitHub Actions if not already enabled
4. The workflow will automatically run on pushes to main/develop branches

### 3. Configure Repository Settings

#### 3.1 Add Repository Secrets (Optional)

For PyPI deployment on releases, add these secrets in your repository settings:

1. Go to Settings → Secrets and variables → Actions
2. Add `PYPI_API_TOKEN` with your PyPI API token

#### 3.2 Configure Branch Protection (Recommended)

1. Go to Settings → Branches
2. Add a rule for the main branch
3. Require status checks to pass before merging

### 4. Test the Setup

#### 4.1 Local Testing

```bash
# Clone your repository
git clone https://github.com/your-username/showdown_gym.git
cd showdown_gym

# Install dependencies
pip install -r requirements-colab.txt

# Test the Colab environment
python colab_environment.py
```

#### 4.2 GitHub Actions Testing

1. Make a small change to your repository
2. Push to the main branch
3. Check the Actions tab to see if the workflow runs successfully

### 5. Using the Colab Notebook

#### 5.1 Direct Access

Users can access your notebook directly via:
```
https://colab.research.google.com/github/your-username/showdown_gym/blob/main/colab_setup.ipynb
```

#### 5.2 Customizing the Notebook

Edit `colab_setup.ipynb` to customize:
- Installation steps
- Example code
- Training configurations
- Documentation

## 🔧 Customization Options

### Custom Environment Configuration

Edit `colab_environment.py` to customize:
- Server configuration
- Environment variables
- Resource optimization
- Error handling

### Custom Requirements

Modify `requirements-colab.txt` to include:
- Additional Python packages
- Specific versions
- Colab-specific optimizations

### Custom Workflow

Edit `.github/workflows/colab-deployment.yml` to:
- Add custom tests
- Configure deployment triggers
- Set up notifications
- Add security checks

## 📊 Monitoring and Analytics

### GitHub Actions Dashboard

Monitor your deployments:
1. Go to Actions tab in your repository
2. View workflow runs and logs
3. Check for failures and debug issues

### Colab Usage Analytics

Track notebook usage:
1. Go to Google Colab
2. View your notebook analytics
3. Monitor user engagement

## 🐛 Troubleshooting

### Common Issues

#### 1. GitHub Actions Failures

**Problem**: Workflow fails to run
**Solution**: 
- Check repository permissions
- Verify workflow file syntax
- Check branch protection rules

#### 2. Colab Import Errors

**Problem**: Cannot import showdown_gym
**Solution**:
- Ensure repository is public
- Check notebook path
- Verify package installation

#### 3. Server Connection Issues

**Problem**: Pokemon Showdown server not starting
**Solution**:
- Check Node.js installation
- Verify server configuration
- Review error logs

### Debug Commands

```bash
# Check GitHub Actions logs
gh run list
gh run view <run-id>

# Test Colab environment locally
python -m pytest tests/ -v

# Validate notebook
jupyter nbconvert --to python colab_setup.ipynb
```

## 🚀 Advanced Features

### 1. Automated Testing

Add automated tests to your workflow:

```yaml
- name: Run tests
  run: |
    python -m pytest tests/ -v --cov=showdown_gym
```

### 2. Performance Monitoring

Monitor Colab performance:

```python
# Add to your notebook
import psutil
print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")
```

### 3. Custom Badges

Add custom badges to your README:

```markdown
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/showdown_gym/blob/main/colab_setup.ipynb)
[![GitHub Actions](https://github.com/your-username/showdown_gym/workflows/Deploy%20to%20Google%20Colab/badge.svg)](https://github.com/your-username/showdown_gym/actions)
```

## 📚 Additional Resources

### Documentation

- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pokemon Showdown Documentation](https://github.com/smogon/pokemon-showdown)

### Community

- [GitHub Discussions](https://github.com/UoA-CARES/showdown_gym/discussions)
- [Issues and Bug Reports](https://github.com/UoA-CARES/showdown_gym/issues)

### Examples

- [Sample Training Scripts](examples/)
- [Configuration Templates](templates/)
- [Best Practices Guide](docs/best-practices.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Colab
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [troubleshooting section](#-troubleshooting)
2. Search existing [issues](https://github.com/UoA-CARES/showdown_gym/issues)
3. Create a new issue with detailed information
4. Contact the maintainers

---

**Happy coding! 🎮⚡**
