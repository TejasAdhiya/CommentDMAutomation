/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ['scontent.cdninstagram.com', 'scontent-*.cdninstagram.com'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.cdninstagram.com',
      },
    ],
  },
}

module.exports = nextConfig
