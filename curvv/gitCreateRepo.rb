require 'net/http'
require 'json'
require 'uri'


repoName = ARGV[1]
repoType = ARGV[2]
token = ARGV[0]

def string_to_boolean(str)
  return true if str.is_a?(String) && (str.downcase == 'true' || str == '1')
  return false if str.is_a?(String) && (str.downcase == 'false' || str == '0')
  
  nil  # return nil if the string is not recognized
end

repoType = string_to_boolean(repoType)

uri = URI('https://api.github.com/user/repos')

# Set up the HTTP request
request = Net::HTTP::Post.new(uri)
request.content_type = 'application/json'
request['Authorization'] = "token #{token}"
request['User-Agent'] = 'Ruby'

# Repository data
request.body = JSON.dump({
  name: repoName,
  description: '',
  private: repoType # Set to true for a private repo
})

# Make the request
response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
  http.request(request)
end

# Handle the response
case response
when Net::HTTPSuccess
  puts "Repository created: #{JSON.parse(response.body)['html_url']}"
else
  puts "Error creating repository: #{response.message}"
end
