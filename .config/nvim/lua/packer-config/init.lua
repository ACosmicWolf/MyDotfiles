return require'packer'.startup(function()
	use 'wbthomason/packer.nvim'
	use 'shaunsingh/nord.nvim'
	use 'kyazdani42/nvim-tree.lua'
	use 'kyazdani42/nvim-web-devicons'
    use 'neovim/nvim-lspconfig'
    use 'rcarriga/nvim-notify'
    use 'nvim-lualine/lualine.nvim'
    use 'romgrk/barbar.nvim'
    use 'nvim-telescope/telescope.nvim'
    use 'nvim-lua/plenary.nvim'
    use 'EdenEast/nightfox.nvim'
    use {'startup-nvim/startup.nvim', config = function() require"startup".setup() end}
    use 'ms-jpq/coq_nvim'
    use 'ms-jpq/coq.artifacts'
    use 'ms-jpq/coq.thirdparty'
    use 'github/copilot.vim'
end)
