module PagesHelper
  def get_image_text(filename)
    path = Rails.root.join('public').to_s
    response = %x(python #{path}/ocr.py public/pictures/#{filename})
  end
end
