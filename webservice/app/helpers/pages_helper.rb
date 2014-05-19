module PagesHelper
  def get_image_text(filename)
    path = Rails.root.join('python').to_s
    response = %x(python #{path}/ocr.py public/pictures/#{filename})
  end

  def get_rate(text)
    path = Rails.root.join('python').to_s
    name = Time.now.to_i
    tmp_filename = "#{name}.txt"
    File.open(Rails.root.join('public', 'pictures', tmp_filename), 'wb') do |file|
      file.write(text)
      file.close
    end
    rate = %x(python #{path}/info_classifier.py public/pictures/#{tmp_filename})
    File.delete(Rails.root.join('public', 'pictures', tmp_filename))
    rate
  end
end
